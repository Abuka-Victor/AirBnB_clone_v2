#!/usr/bin/python3
"""
A simple flask script to start up an app
"""
from flask import Flask
from flask import render_template
from models import storage
from models.state import State
app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def state_list():
    list_of_states = storage.all(State)
    return render_template('7-states_list.html', states=list_of_states)


if __name__ == "__main__":
    app.run(host="0.0.0.0")
