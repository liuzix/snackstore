from flask import Flask
from flask import jsonify
from sqlalchemy import create_engine

app = Flask(__name__)

@app.route('/')
def hello_world():
    return jsonify(msg = "Welcome to Snackstore")

if __name__ == '__main__':
    app.run()
