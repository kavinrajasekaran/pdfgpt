# app.py

from flask import Flask, render_template, request
import pytesseract 
from pdf2image import convert_from_path 

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("upload_form.html")

@app.route("/extract", methods=["POST"])
def extract():
    f = request.files["file"]
    images = convert_from_path(f.filename)
    
    full_text = ""
    for pg, img in enumerate(images):
        text = pytesseract.image_to_string(img) 
        full_text += text
    
    return render_template("upload_form.html", text=full_text) 
    
if __name__ == "__main__":
    app.run()