import numpy as np
from flask import Flask, request, jsonify, render_template
from PIL import Image
import pytesseract
import pandas as pd
import pickle
from sklearn.feature_extraction.text import CountVectorizer
from waitress import serve
from gevent.pywsgi import WSGIServer

pytesseract.pytesseract.tesseract_cmd = r'C:/Program Files/Tesseract-OCR/tesseract.exe'

app = Flask(__name__)
model = pickle.load(open("model.pkl", "rb"))


@app.route("/")
def Home():
    return render_template("main.html")

@app.route("/textdetect")
def text():
    return render_template("index.html")

@app.route("/textdetect", methods=["POST"])
def fetchData():
    if request.method == "POST":
        img = request.form['image']
        im = Image.open(img)
        text = pytesseract.image_to_string(im, lang = 'eng')
        print(text)
        file = pd.read_excel("ProductBrand_dataset.xls")
        output = str()
        text1 = text.lower()
        flag = False
        for txt in file['Brand']:
            st = txt.lower()
            if(st in text1):
                flag = True
        if(flag == True):
            output = "Real Product"
        else:
            output = "Fake Product"

    return render_template("index.html", prediction_text= "{}".format(output))
    #return jsonify(output)

@app.route("/reviewtext")
def reviewd():
    return render_template("ReviewDetection.html")

@app.route("/reviewtext", methods=["POST"])
def reviewfetchData():
    rev = ""
    if request.method=="POST":
        rev = request.form['review']
    v = CountVectorizer()
    finalfeatures = v.transform(rev)
    m = model.predict(finalfeatures)
    print(m)

    #return render_template("ReviewDetection.html", prediction= "{}".format(m))
    return jsonify(m)


if __name__ == "__main__":
    #http_server = WSGIServer(('', 5000), app)
    #http_server.serve_forever()
    app.run(debug=True)