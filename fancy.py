#!/usr/bin/env python

from flask import Flask, render_template

app = Flask(__name__)

items = [
    {'name': 'asdf', 'value': 1234},
    {'name': 'qwer', 'value': 5678},
    {'name': 'zxcv', 'value': 90},
]

@app.route('/')
def index():
    return render_template('index.html', items=items)

if __name__ == '__main__':
    app.run(debug=True)
