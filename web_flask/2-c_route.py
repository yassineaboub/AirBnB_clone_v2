from flask import Flask,render_template
app = Flask(__name__)
app.url_map.strict_slashes = False

@app.route('/')
def hello_HBNB():
    return 'Hello HBNB!'

@app.route('/hbnb')
def dsp_HBNB():
    return 'HBNB'

@app.route('/c/<text>')
def c_HBNB(text):
    return ('C {}'.format(text.replace('_', ' ')))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
