from flask import Flask, jsonify, request
from flask_cors import CORS
from controllers import people
from werkzeug import exceptions
import sqlite3

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return jsonify({'message': 'Hello from futureproof DB!'}), 200

@app.route('/people', methods=['GET', 'POST'])
def people_handler():
  fns = {
    'GET': people.index,
    'POST': people.create
  }
  resp, code = fns[request.method](request)
  return jsonify(resp), code

if __name__ == "__main__":
    app.run(debug=True)