#!/usr/bin/python3
"""
A simple flask script to start up an app
"""
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """ Return hello hbnb"""
    return "Hello HBNB!"
