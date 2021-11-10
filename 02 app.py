import os
from flask import Flask, jsonify
from flask.helpers import send_from_directory

app = Flask(__name__)

@app.route("/")
def root():
  return "Hello World", 200

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.route("/json/<int:a>")
def json(a: int):
  things = { "stuff" : [a,a,a,a] }
  return jsonify(things)