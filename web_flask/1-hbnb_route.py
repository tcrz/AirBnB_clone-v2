#!/usr/bin/python3
"""
script that starts a Flask web application:
- web application must be listening on 0.0.0.0, port 5000
- Routes:
- /: display “Hello HBNB!”
- /hbnb: display "HBNB"
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


if __name__ == "__main__":
    app.run()
