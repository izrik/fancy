#!/usr/bin/env python

from flask import Flask, render_template
import requests
import json

with open('.token') as f:
    tokens = f.read().splitlines()

app = Flask(__name__)


@app.route('/')
def index():

    resp = requests.get('https://api.github.com/notifications',
                        headers={'Authorization': 'token ' + tokens[0]})
    items = json.loads(resp.text)

    return render_template('index.html', items=items)

if __name__ == '__main__':
    app.run(debug=True)
