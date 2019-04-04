#!/usr/bin/env python3
from flask import Flask
from flask import jsonify
from flask import json
from flask import abort
from store import store_api
from staff import staff_api
from auth import auth_api

app = Flask(__name__)
app.register_blueprint(store_api)
app.register_blueprint(staff_api)
app.register_blueprint(auth_api)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
