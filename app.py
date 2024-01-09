#app.py

from flask import Flask, render_template, request 
import pytesseract
from pdf2image import convert_from_path

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        f = request.files["file"]
        images = convert_from_path(f.filename)
            
        full_text = ""
        for pg, img in enumerate(images):
            text = pytesseract.image_to_string(img)
            full_text += text

        return render_template("index.html", text=full_text)

    return render_template("index.html")

if __name__ == "__main__":
   app.run()