from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient
from pymongo.errors import PyMongoError

app = Flask(__name__)

MONGO_URI = "mongodb+srv://22utkarshkapoor:8t4L3DS63RrrcvKt@flaskbasictest.pqdrlan.mongodb.net/?retryWrites=true&w=majority&appName=FlaskBasicTest"
client = MongoClient(MONGO_URI)
db = client["mydatabase"]
collection = db["submissions"]

@app.route('/', methods=['GET', 'POST'])
def form():
    error = None
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')

        if not name or not email:
            error = "All fields are required."
        else:
            try:
                collection.insert_one({'name': name, 'email': email})
                return redirect(url_for('success'))
            except PyMongoError as e:
                error = f"Database error: {str(e)}"

    return render_template('form.html', error=error)

@app.route('/success')
def success():
    return render_template('success.html')

if __name__ == '__main__':
    app.run(debug=True)
