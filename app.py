from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route("/")
def index():
    response_api = requests.get('https://api.github.com/users/guilhermegwt/repos')
    data = response_api.json()

    return render_template('index.html', data=data)
