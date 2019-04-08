from flask import Blueprint
from flask import jsonify
from flask import json
from flask import abort
from flask import request
from db import db

staff_api = Blueprint('staff_api', __name__)

@staff_api.route('/staff_api')
def hello_world():
    return jsonify(msg = "Welcome to Snackstore")

@staff_api.route('/staff_api/getsnacks/<offset>/<limit>')
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

@staff_api.route('/staff_api/countsnacks')
def count_snacks():
    print("editting snacks")
    try:
        result = db.execute("SELECT COUNT(*) FROM snacks")
        return jsonify(result.fetchone()[0])
    except ValueError as e:
        return jsonify(msg = e.args), 400
    else:
        abort(404)
        
@staff_api.route('/staff_api/editsnacks',  methods=['POST'])
def edit_snacks():
    print("editting snacks1")
    req = request.get_json()
    
    print(req)
    
    
    sid = int(req['sid'])
    qty = int(req['qty'])
    #return jsonify(msg = "Welcome to Snackstore")
    
    try:
        sql = "UPDATE snacks SET inventory = %d WHERE sid = %d" % (qty, sid)
        print(sql)
        result = db.execute(sql)
        print("getting result")
        #print(result.fetchone())
        return jsonify(msg = "Done"), 200
    except ValueError as e:
        return jsonify(msg = e.args), 400
    else:
        abort(404)
        
#UPDATE table_name
#SET column1 = value1, column2 = value2, ...
#WHERE condition;


# npm install --save vue-input-autowidth
