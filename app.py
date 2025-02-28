from flask import Flask
from flask import request, render_template
import google.generativeai as genai
import os
from textblob import TextBlob

"""
https://flask.palletsprojects.com/en/stable/quickstart/
https://blog.miguelgrinberg.com/post/why-do-we-pass-name-to-the-flask-class
WSGI protocol: https://wsgi.readthedocs.io/en/latest/what.html 
'ter' : built in convenience from python to help with code
Style for flask: all webpages in templats and everything else in static

pip install -r requirements.txt

Would help to have a venv too
"""
api = os.getenv("makersuite")
genai.configure(api_key=api)
model = genai.GenerativeModel('gemini-1.5-flash')

app = Flask(__name__)

@app.route("/",methods=["GET","POST"])
#landing page is always index
def index():
    return render_template("index.html")

@app.route("/makersuite",methods=["GET","POST"])
#landing page is always index
def makersuite():
    return render_template("makersuite.html")

@app.route("/gemini",methods=["GET","POST"])
def gemini():
    q = request.form.get("q")
    r = model.generate_content(q)
    return(render_template("gemini.html",r= r.candidates[0].content.parts[0].text))

@app.route("/sentiment",methods=["GET","POST"])
def sentiment():
    return render_template("sentiment.html")

@app.route("/textblob_result",methods=["GET","POST"])
def textblob_result():
    q = request.form.get("q")
    r = TextBlob(q).sentiment
    return(render_template("textblob_result.html",r=r ))


if __name__ == "__main__":
    app.run()