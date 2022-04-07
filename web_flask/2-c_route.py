#!/usr/bin/python3
"""
script that starts a Flask web application:
- web application must be listening on 0.0.0.0, port 5000
- Routes:
- /: display “Hello HBNB!”
- /hbnb: display "HBNB"
- /c/<text>: display “C ”, followed by the value of the text variable
- use the option strict_slashes=False in your route definition
"""

from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_route():
    """Flask web application that displays 'Hello HBNB' at route:'/' """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def HBNB_route():
    """Flask web application that displays 'HBNB' at route:'/hbnb' """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_route(text):
    """/c/<text>: display “C ”, followed by the value of the text variable
(replace underscore _ symbols with a space)"""
    return "C " + text.replace("_", " ")


if __name__ == "__main__":
    app.run(host='0.0.0.0')
