""" Main App """
import os

from flask import Flask, jsonify

from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_restful import Resource, Api

app = Flask(__name__)

app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
ma = Marshmallow(app)
api = Api(app)

from models import (
  Entry,
  EntryGenerator,
  Note,
  Status,
  User
)

from schemas import (
  UserSchema,
  EntrySchema
)

users_schema = UserSchema(many=True)
entries_schema = EntrySchema(many=True)

class EntryList(Resource):
  def get(self):
    result = entries_schema.dump(Entry.query.all())
    return jsonify({ "entries": result.data })

  # def put(self, todo_id):
  #   todos[todo_id] = request.form['data']
  #   return {todo_id: todos[todo_id]}


api.add_resource(EntryList, '/entries')