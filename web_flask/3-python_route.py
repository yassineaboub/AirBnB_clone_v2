#!/usr/bin/python3
from flask import Flask, render_template
app = Flask(__name__)
app.url_map.strict_slashes = False
"""script that starts a Flask web application"""


@app.route('/')
def hello_HBNB():
    return 'Hello HBNB!'
"""print Hello HBNB"""


@app.route('/hbnb')
def dsp_HBNB():
    return 'HBNB'
"""print HBNB"""


@app.route('/c/<text>')
def c_HBNB(text):
    return ('C {}'.format(text.replace('_', ' ')))
"""print  “C ” followed by value"""


@app.route('/python', defaults={'text': 'is cool'})
@app.route('/python/<text>')
def Python_HBNB(text):
    return ('Python {}'.format(text.replace('_', ' ')))
"""print "Python ”, followed by value """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
