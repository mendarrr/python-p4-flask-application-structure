#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

# @aoo.route decorator registers the index() function with the Flask application instance app
@app.route('/')
def index():
    return '<h1>Welcome to my page!</h1>'

@app.route('/<string:username>')
def user(username):
    return f'<h1>Profile for {username}</h1>'

if __name__ == '__main__':
    app.run(port=5555, debug=True)
