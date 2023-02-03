# & "f:/Fake Product Identification Project/new_environment/Scripts/Activate.ps1"
import numpy as np
from flask import Flask, request, jsonify, render_template
from PIL import Image
import pytesseract
import pandas as pd
import pickle
#import rds_db as db
import numpy as np
import cv2
from sklearn.feature_extraction.text import CountVectorizer

pytesseract.pytesseract.tesseract_cmd = r'C:/Program Files/Tesseract-OCR/tesseract.exe'

app = Flask(__name__)
#model = pickle.load(open("model.pkl", "rb"))

@app.route("/")
def Home():
    #return render_template("Registration.html")
    return render_template("index.html")

@app.route("/textdetect")
def text():
    return render_template("index.html")

@app.route("/textdetect", methods=["POST"])
def fetchData():
    if request.method == "POST":
        img = request.form['image']
        #im = Image.open(img)
        #text = pytesseract.image_to_string(im, lang = 'eng')
        image = cv2.imread(img)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        text = pytesseract.image_to_string(gray)
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


'''@app.route("/reviewtext")
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
    return jsonify(m)'''

'''@app.route('/login', methods=['post'])
def loginuser():
    name = request.form['name']
    passwd = request.form['passwd']
    account = db.get_details(name, passwd)
    print(account, type(account))
    if not account:
        msg = 'Incorrect username / password !'
        return render_template('Registration.html', check = "{}".format(msg))
    elif account[0]==name and account[1]==passwd:
        msg = "Login Successful"
        return render_template('main.html')
    

@app.route('/insert',methods = ['post'])
def insert():
    
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        passwd = request.form['pass']
        cpasswd = request.form['cpass']
        db.insert_details(name,email,phone, passwd, cpasswd)
        return render_template('Registration.html')'''

if __name__ == "__main__":
    #http_server = WSGIServer(('', 5000), app)
    #http_server.serve_forever()
    app.run(debug=True)