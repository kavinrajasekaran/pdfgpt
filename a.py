from flask import Flask, request, render_template
from pdf2image import convert_from_path
import pytesseract
import os
import openai

# input your own api key, can't post onto github with my api key

openai.api_key = ''

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def upload_file():
    pdf_text = None  # Initialize pdf_text to None
    summarized_text = None  # Initialize summarized_text to None

    if request.method == 'POST':
        uploaded_file = request.files.get('file')
        if uploaded_file:
            # Save the uploaded file to a temporary location
            uploaded_file.save("temp.pdf")

            # Convert PDF to images
            pages = convert_from_path("temp.pdf")

            # Perform OCR on each image and concatenate the text
            pdf_text = ""
            for page in pages:
                # Save the image temporarily for OCR
                page.save("temp.png")

                # Perform OCR on the image
                page_text = pytesseract.image_to_string("temp.png", lang='eng')
                pdf_text += page_text + "\n"

                # Delete the temporary image
                os.remove("temp.png")

            # Delete the temporary PDF file
            os.remove("temp.pdf")

            # Call the OpenAI chatbot API to summarize the extracted text
            response = openai.Completion.create(
                engine="text-davinci-003",  # Replace with the engine you want to use
                prompt=pdf_text,
                temperature=0.7,
                max_tokens=150
            )

            # Extract the summarized text from the response
            summarized_text = response.choices[0].text.strip()
    return render_template('a.html', pdf_text=pdf_text, summarized_text=summarized_text)


if __name__ == '__main__':
    app.run(debug=True)
