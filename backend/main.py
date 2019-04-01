#!/usr/bin/env python3
from flask import Flask
from flask import jsonify
from flask import json
from flask import abort
from sqlalchemy import create_engine

app = Flask(__name__)

db = create_engine('postgres://zl2683:CS4111@34.73.21.127/proj1part2')

@app.route('/api')
def hello_world():
    return jsonify(msg = "Welcome to Snackstore")

@app.route('/api/getsnacks/<offset>/<limit>')
def get_snacks(offset, limit):
    try:
        result = db.execute("SELECT * FROM snacks LIMIT {} OFFSET {}".format(int(limit), int(offset)))
        ret = []
        for row in result:
            r = dict(row.items())
            ret.append(r)
        return jsonify(ret)
    except ValueError as e:
        return jsonify(msg = e.args), 400
    else:
        abort(404)

@app.route('/api/countsnacks')
def count_snacks():
    try:
        result = db.execute("SELECT COUNT(*) FROM snacks")
        return jsonify(result.fetchone()[0])
    except ValueError as e:
        return jsonify(msg = e.args), 400
    else:
        abort(404)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
