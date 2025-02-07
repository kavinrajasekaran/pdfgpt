# **pdfGPT**

## **Overview**
This Flask web application allows users to **upload a PDF file**, extract text using **OCR (Optical Character Recognition)**, and generate a **summarized version** of the extracted text using **OpenAI's GPT model**.

## **How It Works**
### **1. Upload a PDF**
- Open the web application in a browser.
- Click the **"Choose File"** button to upload a PDF document.

### **2. Processing the File**
Once the file is uploaded, the application will:
- Convert the PDF pages into images.
- Extract text from the images using OCR (`pytesseract`).
- Summarize the extracted text using OpenAI’s `gpt-3.5-turbo` model.

### **3. Viewing Results**
- The original extracted text and the summarized version will be displayed on the webpage.

## **Installation & Setup**
### **1. Clone the Repository**
```sh
git clone https://github.com/yourusername/flask-pdf-summarizer.git
cd flask-pdf-summarizer
```

### **2. Install Dependencies**
Ensure you have Python installed, then install the required packages:
```sh
pip install -r requirements.txt
```

Additionally, install **Poppler** (required for `pdf2image`):
- **Ubuntu:** `sudo apt install poppler-utils`
- **Mac (Homebrew):** `brew install poppler`
- **Windows:** Download from [Poppler for Windows](http://blog.alivate.com.au/poppler-windows/)

### **3. Set Your OpenAI API Key**
Create an **environment variable** for security:
```sh
export OPENAI_API_KEY="your_api_key_here"  # For Mac/Linux
set OPENAI_API_KEY="your_api_key_here"  # For Windows
```
Or add it to a `.env` file and load it in your app.

### **4. Run the Application**
Start the Flask app:
```sh
python app.py
```
The app will be accessible at `http://127.0.0.1:5000/`.

## **Technologies Used**
- **Flask** – Web framework for handling requests & file uploads.  
- **pdf2image** – Converts PDF pages to images.  
- **pytesseract** – OCR library for text extraction.  
- **OpenAI API** – Summarizes extracted text.  
- **tempfile** – Handles temporary files securely.  

## **Potential Enhancements**
- 🔹 **Multi-language OCR support**  
- 🔹 **Support for DOCX and TXT files**  
- 🔹 **Pagination for large text outputs**  

---
Enjoy using the **Flask PDF Summarization App!** 🚀


