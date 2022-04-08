#!/usr/bin/python3
"""
script that starts a Flask web application:
- Use storage for fetching data from the storage engine 
(FileStorage or DBStorage) => from models import storage and storage.all(...)
- After each request you must remove the current SQLAlchemy Session:
- Declare a method to handle @app.teardown_appcontext
- Call in this method storage.close()
Routes:
- /states_list: display a HTML page: (inside the tag BODY)
- H1 tag: “States”
- UL tag: with the list of all State objects present in DBStorage sorted
by name (A->Z)
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


@app.route('/states_list', strict_slashes=False)
def states_list():
    """Flask web application that displays <states> and <states.id> 
at route:'/states_list' """
    state_dict = storage.all(State)
    # print(state_dict)
    return render_template('7-states_list.html', state_dict=state_dict)


if __name__ == "__main__":
    app.run()
