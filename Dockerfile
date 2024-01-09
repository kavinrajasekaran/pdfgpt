FROM python:3.9.6

# Install dependencies
RUN apk add --update \
    tesseract-ocr \
    libtesseract-dev \
    poppler-utils

# Install Tesseract data
RUN wget https://github.com/tesseract-ocr/tessdata/raw/master/eng.traineddata && \
    mv eng.traineddata /usr/share/tessdata/

# Set environment variables  
ENV TESSDATA_PREFIX=/usr/share/tessdata
ENV PYTESSERACT_PATH=/usr/bin/tesseract
ENV POPPLER_PATH=/usr/bin

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

ENV FLASK_APP=a.py

EXPOSE 5000 

CMD ["flask", "run", "--host=0.0.0.0"]