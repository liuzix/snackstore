from flask import Blueprint
from flask import jsonify
from flask import json
from flask import abort
from flask import request
import redis
import uuid
import traceback
from db import db
from db import Session

auth_api = Blueprint('auth_api', __name__)

r = redis.from_url("redis://h:p5bf43139967faa22b3620e1a2d89b2c3c18ca7" \
    "94cfa84f2d6c57c50173144e62@ec2-23-21-34-34." \
    "compute-1.amazonaws.com:19729")

class SnackStoreUser:
    def __init__(self, key = ""):
        if key != "":
            self.key = key
            self.data = json.loads(r.get(key))
            print(self.data)
        else:
            self.key = ""
            self.data = {}

    def commit(self):
        if self.key == "":
            self.key = uuid.uuid4().hex + self.data['login']
        r.set(self.key, json.dumps(self.data))

@auth_api.route("/api/user_info", methods=['GET'])
def user_info():
    key = request.get_cookie('tag')
    if key == "":
        return jsonify(logged_in = False), 200
    user = SnackStoreUser(key)
    return jsonify(logged_in = True, data = user.data), 200


@auth_api.route("/api/signup_customer", methods=['POST'])
def signup_customer():
    session = Session()
    print(request.data)
    req = request.get_json()

    login = req['login']
    if login == '':
        return jsonify(msg="login cannot be empty"), 400

    name = req['name']
    if name == '':
        return jsonify(msg="name cannot be empty"), 400
    
    password = req['password']
    if password == '':
        return jsonify(msg="password cannot be empty"), 400

    address = req['address']
    if address == '':
        return jsonify(msg="address cannot be empty"), 400

    try:
        res = session.execute("INSERT INTO customers (name, address) "\
            "VALUES (:name, :address) RETURNING *", {"name": name, "address": address})
        cid = res.fetchone()[0]
        print("new user cid = {}".format(cid))

        res = session.execute("INSERT INTO login (loginName, password, cid, eid)"\
            "VALUES (:login, :password, :cid, NULL)", 
            {"login": login, "password": password, "cid": cid})

    
        user = SnackStoreUser()
        user.data['login'] = login
        user.data['name'] = name
        user.data['cart'] = []
        user.commit()

        session.commit()        
    except Exception as e:
        session.rollback()
        traceback.print_exc()
        return jsonify(msg=e.args[0]), 400

    ret = jsonify(msg="success")
    ret.set_cookie('tag', user.key)
    return ret, 200
