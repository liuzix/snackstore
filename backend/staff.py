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
        result = db.execute("SELECT * FROM snacks ORDER BY sid LIMIT {} OFFSET {}".format(int(limit), int(offset)))
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
        
@staff_api.route('/staff_api/getorders/<offset>/<limit>')
def get_orders(offset, limit):
    try:
        result = db.execute(
                "select customers.name, customers.address, customers.cid, " \
                "customerorders1.oid, customerorders1.date, customerorders1.status" \
                " from (select * from customerorders left outer join staff on customerorders.eid = staff.eid) " \
                "as customerorders1 join customers on customerorders1.cid = customers.cid " \
                "ORDER BY customerorders1.oid DESC LIMIT {} OFFSET {}".format(int(limit), int(offset)))
        
        ret = []
        for row in result:
            r = dict(row.items())
            sub_result = db.execute("""
                SELECT c.quantity, s.name, s.cost FROM customersuborders AS c, snacks AS s
                WHERE c.oid = {} AND c.sid = s.sid 
            """.format(int(row['oid'])))
            r['suborders'] = []
            for sub_row in sub_result:
                r['suborders'].append(dict(sub_row.items()))
            ret.append(r)
        return jsonify(ret)
    except ValueError as e:
        return jsonify(msg = e.args), 400
    else:
        abort(404)
        
@staff_api.route('/staff_api/countorders')
def count_orders():
    print("counting orders")
    try:
        result = db.execute("SELECT COUNT(*) FROM customerorders")
        return jsonify(result.fetchone()[0])
    except ValueError as e:
        return jsonify(msg = e.args), 400
    else:
        abort(404)
        
@staff_api.route('/staff_api/togglecomplete', methods=['POST'])
def toggle_complete():
    req = request.get_json()
    completion = req['status']
    oid = req['oid']

    db.execute("""
        UPDATE customerorders SET status = %s WHERE oid = %s
    """, completion, oid)

    return jsonify(msg = "successs"), 200



@staff_api.route('/staff_api/deleteorder',  methods=['POST'])
def delete_order():
    print("deleting order")
    req = request.get_json()
    
    print(req)
    
    oid = int(req['oid'])

    try:
        sql = "DELETE FROM customerorders WHERE customerorders.oid = %d;" % (oid)
        print(sql)
        db.execute(sql)
        print("getting result")
        #print(result.fetchone())
        return jsonify(msg = "Done"), 200
    except ValueError as e:
        return jsonify(msg = e.args), 400
    else:
        abort(404)
        
@staff_api.route('/staff_api/getsuppliers/<offset>/<limit>')
def get_suppliers(offset, limit):
    try:
        result = db.execute(
   "select * from suppliers, staff where suppliers.maintainer " \
   "= staff.eid ORDER BY suppliers.spid DESC LIMIT {} OFFSET {}".format(int(limit), int(offset)))
        ret = []
        for row in result:
            r = dict(row.items())
            ret.append(r)
        return jsonify(ret)
    except ValueError as e:
        return jsonify(msg = e.args), 400
    else:
        abort(404)
        
@staff_api.route('/staff_api/countsuppliers')
def count_suppliers():
    print("counting suppliers")
    try:
        result = db.execute("SELECT COUNT(*) FROM suppliers")
        return jsonify(result.fetchone()[0])
    except ValueError as e:
        return jsonify(msg = e.args), 400
    else:
        abort(404)  
        
@staff_api.route('/staff_api/addsuppliers',  methods=['POST'])
def add_suppliers():
    print("adding suppliers")
    
    
    req = request.get_json()    
    print(req)
    name = req['name']
    address = req['address']
    phone_number = req['phone_number']
    sql =  "INSERT INTO suppliers(spid, address, name, status, maintainer, phone_number) "\
    "VALUES " \
    "(default, '%s', '%s', 'active', 1, '%s') RETURNING * " % (address, name, phone_number)
    print(sql)
    #result = db.execute(sql)
    #print(result)
    try:
        result = db.execute(
            """INSERT INTO suppliers(spid, address, name, status, maintainer, phone_number)
            VALUES (default, %s, %s, 'active', 1, %s) RETURNING * """, address, name, phone_number)
        return jsonify(result.fetchone()[0])
    except ValueError as e:
        return jsonify(msg = e.args), 400
    else:
        abort(404) 
#UPDATE table_name
#SET column1 = value1, column2 = value2, ...
#WHERE condition;


# npm install --save vue-input-autowidth
