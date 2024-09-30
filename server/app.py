#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return "<h1>Python Operations with Flask Routing and Views</h1>"


@app.route("/print/<string:parameter>")
def print_string(parameter):
    print(parameter)
    return parameter


@app.route("/count/<int:param>")
def count(param):
    numbers = range(param)
    result = ""

    for num in numbers:
        result += str(num) + "\n"

    return result


@app.route("/math/<int:num1>/<operation>/<int:num2>")
def math(num1, operation, num2):

    result = None

    # Check operation and perform the appropriate calculation
    if operation == "+" or operation == "%2B":  # Include %2B for URL-encoded '+'
        result = num1 + num2
    elif operation == "-":
        result = num1 - num2
    elif operation == "*":
        result = num1 * num2
    elif operation == "div":
        if num2 != 0:
            result = num1 / num2
        else:
            return "Division by zero is not allowed", 400
    elif operation == "%":
        if num2 != 0:
            result = num1 % num2
        else:
            return "Modulo by zero is not allowed", 400
    else:
        return "Invalid operation", 400

    return str(result)


if __name__ == "__main__":
    app.run(port=5555, debug=True)
