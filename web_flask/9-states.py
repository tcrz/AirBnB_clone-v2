#!/usr/bin/python3
"""
script that starts a Flask web application:
- Use storage for fetching data from the storage engine
(FileStorage or DBStorage) => from models import storage and storage.all(...)
- After each request you must remove the current SQLAlchemy Session:
- Declare a method to handle @app.teardown_appcontext
- Call in this method storage.close()
Routes:
    - /states: display a HTML page: (inside the tag BODY)
        - H1 tag: “States”
        - UL tag: with the list of all State objcts present in DBStorage sorted
        by name
            - LI tag: description of one State: <state.id>: <B><state.name></B>
    - /states/<id>: display a HTML page: (inside the tag BODY)
        - If a State object is found with this id:
            - H1 tag: “State: ”
            - H3 tag: “Cities:”
            - UL tag: with the list of City objects linked to the State
            sorted by name
            - LI tag: description of one City: <city.id>: <B><city.name></B>
        - Otherwise:
            - H1 tag: “Not found!”
"""

from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.teardown_appcontext
def teardown(reponse_or_exc):
    """runs this method when app context tears down"""
    storage.close()


@app.route('/states')
def states_list():
    """Flask web application that displays <states.id> and <states.name>
at route:'/states' """
    state_dict = storage.all(State)
    return render_template('9-states.html', state_dict=state_dict)


@app.route('/states/<id>')
def states_id_list(id):
    """Flask web application that displays <states.id>, <states.name> with
associated <cities.id>, <cities.name> at route:'/cities_by_states' """
    key_id = 'State.' + str(id)
    state_dict = storage.all(State)
    return render_template('9-states.html', state_dict=state_dict,
                           key_id=key_id)


if __name__ == "__main__":
    app.run()
