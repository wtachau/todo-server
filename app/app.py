""" Main App """
import os
from datetime import datetime

from flask import Flask, jsonify, session
from flask import request

from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_restful import Resource, Api, reqparse


app = Flask(__name__)

app.secret_key = os.environ['SECRET_KEY']

app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
ma = Marshmallow(app)
api = Api(app)

entry_parser = reqparse.RequestParser()
entry_parser.add_argument('type')
entry_parser.add_argument('text')
entry_parser.add_argument('entries')

from models import (
  Entry,
  EntryGenerator,
  Note,
  Status,
  User,
  Type
)

from schemas import (
  UserSchema,
  EntrySchema,
  TypeSchema
)

users_schema = UserSchema(many=True)
entries_schema = EntrySchema(many=True)
types_schema = TypeSchema(many=True)
entry_schema = EntrySchema()

class EntryAPI(Resource):
  def post(self, todo_id):
    entry = Entry.query.get(todo_id)
    entry.completed_on = datetime.utcnow()
    db.session.commit()
    result = entry_schema.dump(entry)
    return jsonify({"data": result.data})

class EntryListAPI(Resource):
  def get(self):
    user_entries = Entry.query.filter_by(user_id=session['user_id']).all()
    result = entries_schema.dump(user_entries)
    return jsonify({"data": result.data})
  
  def post(self):
    args = entry_parser.parse_args()
    entry_text = args['text'].encode('utf-8')
    type = Type.query.filter_by(id = args.get('type')).one()

    # Find the highest order of existing entries, so the new one will be 1 higher
    # todo: should use http://docs.sqlalchemy.org/en/latest/orm/collections.html#dynamic-relationship-loaders
    existing_entries = Entry.query.filter_by(type=type, completed_on=None).all()
    highest_order = max([entry.order for entry in existing_entries])

    new_entry = Entry(session['user_id'], entry_text, type, highest_order + 1)

    current_db_sessions = db.session.object_session(new_entry)
    current_db_sessions.add(new_entry)
    db.session.commit()

    result = entry_schema.dump(new_entry)
    return jsonify({"data": result.data})

  def patch(self):
    entries_json = request.json["entries"]
    entries = entries_schema.load(entries_json).data

    for index, entry in enumerate(entries):
      entry.order = index + 1
    db.session.commit()

    return jsonify({ "data": entries_schema.dump(entries).data })

class TypeList(Resource):
  def get(self):
    session['user_id'] = 5
    user_types = Type.query.filter_by(user_id=session['user_id']).all()
    result = types_schema.dump(user_types)
    return jsonify({"data": result.data})

@app.before_request
def before_request():
  user_token = request.headers.get("X-User-Token")
  if user_token is None:
    return 'Unauthorized Request', 403

  user = User.query.filter_by(icloud_token=user_token).first()
  if not user:
    user = User(user_token)
    db.session.add(user)
    db.session.commit()

  session['user_id'] = user.id

api.add_resource(EntryListAPI, '/entries', endpoint = 'entries')
api.add_resource(EntryAPI, '/entry/<string:todo_id>', endpoint='entry')

api.add_resource(TypeList, '/types', endpoint = 'types')