from flask import Flask, request, render_template
from pdf2image import convert_from_path
import pytesseract
import cv2
import os
import openai
from PIL import Image

# ==========================
# Configuration
# ==========================
openai.api_key = ''  # Input your OpenAI API key here
app = Flask(__name__)

def preprocess_image(image_path):
    """Preprocess the image to enhance OCR accuracy."""
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    # Resize image for better OCR accuracy
    scale_percent = 200  # Increase size by 200%
    width = int(image.shape[1] * scale_percent / 100)
    height = int(image.shape[0] * scale_percent / 100)
    image = cv2.resize(image, (width, height), interpolation=cv2.INTER_CUBIC)

    # Apply adaptive thresholding for better text contrast
    image = cv2.adaptiveThreshold(image, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                  cv2.THRESH_BINARY, 11, 2)

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

            try:
                # Convert PDF to images (one image per page)
                pages = convert_from_path(temp_pdf_path)
                pdf_text = ""

                for i, page in enumerate(pages):
                    # Save each page as an image
                    temp_image_path = f"temp_{i}.png"
                    page.save(temp_image_path)

                    # Preprocess the image
                    processed_image_path = preprocess_image(temp_image_path)

                    # Extract text using OCR
                    page_text = pytesseract.image_to_string(processed_image_path, lang='eng')
                    pdf_text += page_text + "\n"

                    # Clean up temporary files
                    os.remove(temp_image_path)
                    os.remove(processed_image_path)

                # Remove the temporary PDF file
                os.remove(temp_pdf_path)

                # Call OpenAI API for summarization
                response = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    messages=[
                        {"role": "system", "content": "You are a helpful assistant that summarizes text."},
                        {"role": "user", "content": f"Summarize the following text:\n{pdf_text}"}
                    ],
                    temperature=0.7,
                    max_tokens=150
                )

                # Extract the summarized text from the response
                summarized_text = response['choices'][0]['message']['content'].strip()

            except Exception as e:
                pdf_text = f"Error: {str(e)}"

    return render_template('a.html', pdf_text=pdf_text, summarized_text=summarized_text)

if __name__ == '__main__':
    app.run(debug=True)
