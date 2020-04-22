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

@app.route('/python', defaults={'text':'is cool'})
@app.route('/python/<text>')
def Python_HBNB(text):
    return ('Python {}'.format(text.replace('_', ' ')))

@app.route('/number/<int:n>')
def number_HBNB(n):
    return ('{} is a number'.format(n))

@app.route('/number_template/<int:n>')
def body_HBNB(n):
  return render_template('5-number.html', n=n)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
