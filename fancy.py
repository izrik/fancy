#!/usr/bin/env python

from flask import Flask, render_template
import requests
import json

with open('fancy.json') as f:
    config = json.load(f)

app = Flask(__name__)


@app.route('/')
def index():

    sources = config['sources']
    items = []
    for source in sources:
        type = source['type']
        name = source['name']
        if 'url' in source:
            url = source['url']
        else:
            url = 'https://api.github.com/notifications'
        token = source['token']

        resp = requests.get(url, headers={'Authorization': 'token ' + token})
        if resp.status_code != 200:
            return 500
        items += json.loads(resp.text)

    return render_template('index.html', items=items)

if __name__ == '__main__':
    app.run(debug=True)
