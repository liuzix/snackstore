from flask import Blueprint
from flask import jsonify
from flask import json
from flask import abort
from flask import request
from db import db
from auth import SnackStoreUser

store_api = Blueprint('store_api', __name__)

@store_api.route('/api')
def hello_world():
    return jsonify(msg = "Welcome to Snackstore")

@store_api.route('/api/getsnacks/<offset>/<limit>')
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

@store_api.route('/api/countsnacks')
def count_snacks():
    try:
        result = db.execute("SELECT COUNT(*) FROM snacks")
        return jsonify(result.fetchone()[0])
    except ValueError as e:
        return jsonify(msg = e.args), 400
    else:
        abort(404)

@store_api.route('/api/upload_cart', methods=['POST'])
def update_cart():
    key = request.cookies.get('tag')
    user = SnackStoreUser(key)
    req = request.get_json()
    user.data['cart'] = req
    print(user.data)
    user.commit()
    return jsonify(msg="success"), 200