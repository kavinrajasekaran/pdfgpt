from flask import Flask, request, render_template
from pdf2image import convert_from_path
import pytesseract
import cv2
import numpy as np
import os
import openai
from PIL import Image

# Input your own OpenAI API key
openai.api_key = ''

app = Flask(__name__)

def preprocess_image(image_path):
    """Preprocess the image to enhance OCR accuracy."""
    # Read image using OpenCV
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    # Resize to improve OCR accuracy
    scale_percent = 200  # Increase size by 200%
    width = int(image.shape[1] * scale_percent / 100)
    height = int(image.shape[0] * scale_percent / 100)
    image = cv2.resize(image, (width, height), interpolation=cv2.INTER_CUBIC)

    # Apply adaptive thresholding for better contrast
    image = cv2.adaptiveThreshold(
        image, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2
    )

    # Save the processed image temporarily
    processed_image_path = "processed_temp.png"
    cv2.imwrite(processed_image_path, image)

    return processed_image_path


@app.route('/', methods=['GET', 'POST'])
def upload_file():
    pdf_text = None  # Initialize pdf_text to None
    summarized_text = None  # Initialize summarized_text to None

    if request.method == 'POST':
        uploaded_file = request.files.get('file')
        if uploaded_file:
            # Save the uploaded file to a temporary location
            temp_pdf_path = "temp.pdf"
            uploaded_file.save(temp_pdf_path)

            # Convert PDF to images
            pages = convert_from_path(temp_pdf_path)

            # Perform OCR on each image and concatenate the text
            pdf_text = ""
            for i, page in enumerate(pages):
                # Save the image temporarily
                temp_image_path = f"temp_{i}.png"
                page.save(temp_image_path)

                # Preprocess the image before OCR
                processed_image_path = preprocess_image(temp_image_path)

                # Perform OCR on the processed image
                page_text = pytesseract.image_to_string(processed_image_path, lang='eng')
                pdf_text += page_text + "\n"

                # Delete the temporary images
                os.remove(temp_image_path)
                os.remove(processed_image_path)

            # Delete the temporary PDF file
            os.remove(temp_pdf_path)

            # Call OpenAI API to summarize the extracted text
            response = openai.Completion.create(
                engine="text-davinci-003",  # Replace with the engine you want to use
                prompt=f"Summarize the following text:\n{pdf_text}",
                temperature=0.7,
                max_tokens=150
            )

            # Extract the summarized text from the response
            summarized_text = response.choices[0].text.strip()

    return render_template('a.html', pdf_text=pdf_text, summarized_text=summarized_text)


if __name__ == '__main__':
    app.run(debug=True)
