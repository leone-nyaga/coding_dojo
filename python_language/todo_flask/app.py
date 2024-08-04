#!/usr/bin/python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello dude, nice to meet you!"

@app.route('/flask')
def flask():
    return "this is a flask"


if __name__ == '__main__':
    app.run(debug=True)
