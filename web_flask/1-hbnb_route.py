#!/usr/bin/python3
from flask import Flask
app = Flask(__name__)
app.url_map.strict_slashes = False
"""script that starts a Flask web application"""


@app.route('/')
def hello_HBNB():
    return 'Hello HBNB!'
"""print HBNB"""


@app.route('/hbnb')
def dsp_HBNB():
    return 'HBNB'

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
