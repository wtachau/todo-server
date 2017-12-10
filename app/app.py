import os

from flask import Flask, request, jsonify

from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from models import (
  Entry,
  EntryGenerator,
  Note,
  Status,
  User
)

@app.route("/todos", methods=["GET"])
def test():

  return "Success", 200

@app.route("/users", methods=["GET"])
def users():
  return jsonify(User.query().all())