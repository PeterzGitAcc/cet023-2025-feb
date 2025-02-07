from flask import Flask
from flask import request, render_template

"""
https://flask.palletsprojects.com/en/stable/quickstart/
https://blog.miguelgrinberg.com/post/why-do-we-pass-name-to-the-flask-class
WSGI protocol: https://wsgi.readthedocs.io/en/latest/what.html 
'ter' : built in convenience from python to help with code
Style for flask: all webpages in templats and everything else in static
"""


app = Flask(__name__)

@app.route("/",methods=["GET","POST"])
#landing page is always index
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run()