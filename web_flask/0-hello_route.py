#!/usr/bin/python3
"""Flask package"""

from flask import Flask
import os
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_world():
    """hello world testing"""
    return 'Hello HBNB!'


os.environ['FLASK_APP'] = "./web_flask/0-hello_route.py"
os.system("flask run --host=0.0.0.0")
