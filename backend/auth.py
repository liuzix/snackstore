from flask import Blueprint
from flask import jsonify
from flask import json
from flask import abort
from flask import request
from db import db

auth_api = Blueprint('auth_api', __name__)

@auth_api.route("/api/signup_customer", methods=['POST'])
def signup_customer():
    login = request.args.get('login', '')
    if login == '':
        return jsonify(msg="login cannot be empty"), 400

    name = request.args.get('name', '')
    if name == '':
        return jsonify(msg="name cannot be empty"), 400
    
    password = request.args.get('password', '')
    if password == '':
        return jsonify(msg="password cannot be empty"), 400

    db.execute("")
    
