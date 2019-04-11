from flask import Blueprint
from flask import jsonify
from flask import json
from flask import abort
from flask import request
from db import db
from auth import SnackStoreUser

from db import Session


store_api = Blueprint('store_api', __name__)

@store_api.route('/api')
def hello_world():
    #print("getting hello world")
    return jsonify(msg = "Welcome to Snackstore")

@store_api.route('/api/getsnacks/<offset>/<limit>')
def get_snacks(offset, limit):
    try:
        result = db.execute("SELECT * FROM snacks ORDER BY sid LIMIT {} OFFSET {} ".format(int(limit), int(offset)))
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

@store_api.route('/api/checkout', methods=['POST'])
def checkout():
    key = request.cookies.get('tag')
    user = SnackStoreUser(key)
    session = Session()
    
    res = session.execute("""
        SELECT cid FROM login WHERE loginname = :login
    """, {'login': user.data['login']})

    cid = res.fetchone()[0]
    print('cid = ' + str(cid))
    if cid is None:
        return jsonify(msg="you are a staff"), 400

    res = session.execute("""
        INSERT INTO customerorders (cid, date, status) VALUES (:cid, current_date, 'incomplete') 
        RETURNING *
    """, {'cid': cid})
    oid = res.fetchone()['oid']
    print('old = ' + str(oid))

    for item in user.data['cart']:
        sid = item['sid']
        quantity = item['quantity']
        print("item sid = {}, quantity = {}".format(sid, quantity))
        session.execute("""
            INSERT INTO customersuborders (oid, sid, quantity) VALUES (:oid, :sid, :quantity)
        """, {'oid': oid, 'sid': sid, 'quantity': quantity})

    user.data['cart'] = []
    user.commit()
    session.commit()
    return jsonify(msg="success"), 200

