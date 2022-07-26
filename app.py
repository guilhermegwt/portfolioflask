from app import app
from webbrowser import get
from flask import Flask, render_template
import requests
import os 

if __name__=='main':
    port = int(os.getenv('PORT'), '5000')
    app.run(host='0.0.0.0', port = port)

app = Flask(__name__)

@app.route("/")
def index():
    response_api = requests.get('https://api.github.com/users/guilhermegwt/repos')
    data = response_api.json()

    return render_template('index.html', data=data)
