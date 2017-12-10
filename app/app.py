""" Main App """
import os

from flask import Flask, jsonify

from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

app = Flask(__name__)

app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
ma = Marshmallow(app)

from models import (
  Entry,
  EntryGenerator,
  Note,
  Status,
  User
)

from schemas import (
  UserSchema
)

users_schema = UserSchema(many=True)

@app.route("/users", methods=["GET"])
def users():
  result = users_schema.dump(User.query.all())
  return jsonify({"users": result.data})
