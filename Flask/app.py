from flask import Flask

app = Flask(__name__)

@app.route('/')

def home():
    return "Welcome to the Basic Flask Server!"

@app.route('/about')

def about():
    return "This is a About for the Flask application."

@app.route('/contact/<name>')

def contact(name):
    name = "Hello " + name + "!"
    return name

@app.route('/square/<int:number>')

def square(number):
    result = number * number
    return f"The square of {number} is {result}."

@app.route('/add/<a>/<b>')

def add(a, b):
    result = int(a) + int(b)
    return f"The sum of {a} and {b} is {result}."

if __name__ == '__main__':
    app.run(debug=True)
