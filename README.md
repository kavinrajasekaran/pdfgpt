
# PDFGPT - PDF Text Extraction & Summarization Tool

PDFGPT is a Flask-based web application that allows users to upload a PDF file, extract text from it using Tesseract OCR, and summarize the extracted text using OpenAI's GPT-3.5-turbo model. This project demonstrates how to integrate OCR, text preprocessing, and natural language processing into a single pipeline.

---

## 📌 Features
- Upload a PDF file to extract text from its pages.
- Enhanced OCR accuracy using OpenCV preprocessing.
- Summarization of extracted text using OpenAI’s GPT-3.5-turbo model (Updated from the deprecated text-davinci-003).
- Displays both extracted text and summarized text via a user-friendly web interface.

---

## 📦 Requirements
- Python 3.9+
- Flask
- pdf2image
- pytesseract
- opencv-python-headless
- numpy
- openai
- pillow
- Tesseract-OCR (installed via Homebrew)
- Poppler (installed via Homebrew)

---

## 💻 Installation
### 1. Clone the Repository
```
git clone <your-repo-url>
cd <your-repo-directory>
```

### 2. Install Dependencies
```
pip3 install -r requirements.txt
```

### 3. Install Tesseract & Poppler (For macOS via Homebrew)
```
brew install tesseract
brew install poppler
```

---

## 🚀 Usage
1. Run the Flask app:
```
python3 a.py
```
2. Visit `http://127.0.0.1:5000/` in your browser.
3. Upload a PDF file and click "Upload & Process".

---

## 📂 Folder Structure
```
/project-root
|-- a.py               # Main Flask application
|-- requirements.txt    # Python dependencies file
|-- /templates          # Folder for HTML files
|   |-- a.html          # Front-end interface
```

---

## 🔑 Environment Variable (API Key)
Ensure you have your OpenAI API key set in `a.py`:
```python
openai.api_key = 'your-openai-api-key'
```

---

## 📌 Requirements.txt (Example)
```
Flask
pdf2image
pytesseract
opencv-python-headless
numpy
openai
Pillow
```

---

## 📜 License
This project is licensed under the MIT License - see the LICENSE file for details.

---

## 💡 Acknowledgements
- OpenAI for their GPT-3.5-turbo model.
- Tesseract OCR for text extraction.
- Poppler for PDF rendering.
