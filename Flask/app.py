from flask import Flask

app = Flask(__name__)

@app.route('/')

def home():
    return "Welcome to the Basic Flask Server!"

@app.route('/about')

def about():
    return "This is a About for the Flask application."

if __name__ == '__main__':
    app.run(debug=True)
