"""
An assorted collection of fun tools!
"""
from random import randint
from flask import Flask, request

import models

app = Flask(__name__)


@app.route("/")
def home():
    return "Hello, world!!!"


@app.route("/is_even/<int:n>")
def is_even(n):
    # Returns true if n is even
    if n > 20:
        return "Erro, número maior que 20", 400

    return str(n % 2 == 0)


@app.route("/randn")
def randn():
    # Returns a random integer
    print("Um usuário pediu por um número inteiro!")
    x = randint(0, 100)

    with open("/tmp/log", "w") as f:
        f.write(f"Registrando pedido pelo número {x}")

    print(f"Retornando o número {x}")

    return str(x)


@app.route("/user", methods=["POST", "GET"])
def new_user():

    data = request.get_json()

    email = data.get("email")
    birthday = data.get("birthday")

    if not email:
        return "Email é necessário!", 400

    user = models.User.create(email=email, birthday=birthday)

    return "Usuário criado!"

    # if data:
    #     return data["name"]

    # return "No data!", 200


if __name__ == "__main__":
    app.run(debug=True)
