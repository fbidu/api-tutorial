"""
An assorted collection of fun tools!
"""
from random import randint
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    # Raíz da nossa API!
    return "Hello, API!"

@app.route("/is_even/<int:n>")
def is_even(n):
    # Returns true if n is even
    return str(n % 2 == 0)

@app.route("/randn")
def randn():
    # Returns a random integer
    return str(randint(0, 100))

if __name__ == "__main__":
    app.run(debug=True)