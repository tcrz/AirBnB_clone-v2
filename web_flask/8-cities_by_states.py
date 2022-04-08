#!/usr/bin/python3
"""
script that starts a Flask web application:
- Use storage for fetching data from the storage engine
(FileStorage or DBStorage) => from models import storage and storage.all(...)
- After each request you must remove the current SQLAlchemy Session:
- Declare a method to handle @app.teardown_appcontext
- Call in this method storage.close()
Routes:
    - /cities_by_states: display a HTML page: (inside the tag BODY)
    - H1 tag: “States”
    - UL tag: list of all State objects present in DBStorage sorted by name
    - LI tag: description of 1 State: <state.id>: <B><state.name></B> + UL tag:
        with the list of City objects linked to the State sorted by name (A->Z)
    - LI tag: description of one City: <city.id>: <B><city.name></B>
        - LI tag: description of one State: <state.id>: <B><state.name></B>
"""

from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)


@app.teardown_appcontext
def teardown(reponse_or_exc):
    """runs this method when app context tears down"""
    storage.close()


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states_list():
    """Flask web application that displays <states.id>, <states.name> with
associated <cities.id>, <cities.name> at route:'/cities_by_states' """
    state_dict = storage.all(State)
    return render_template('8-cities_by_states.html', state_dict=state_dict)


if __name__ == "__main__":
    app.run()
