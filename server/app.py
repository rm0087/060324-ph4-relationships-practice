#!/usr/bin/env python3

from flask import request
from config import app, db
# from models import MODELS GO HERE

@app.get('/')
def index():
    return "Hello world"

# write your routes here!

if __name__ == '__main__':
    app.run(port=5555, debug=True)
