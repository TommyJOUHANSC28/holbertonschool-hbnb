#!/usr/bin/python3
from flask import Flask
from app import create_app

app = create_app('development')

app = Flask(__name__)

@app.route('/')
def index():
    return "Welcome to HBnB"

app.run(host="localhost", port=5000, debug=True)
