""" Main App """
import os

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

class EntryResource(Resource):
  def post(self):
    args = entry_parser.parse_args()
    entry_text = str(args['text'])
    type = Type.query.filter_by(id = args.get('type')).one()

    new_entry = Entry(session['user_id'], entry_text, type)

    current_db_sessions = db.session.object_session(new_entry)
    current_db_sessions.add(new_entry)
    db.session.commit()
    
    result = entry_schema.dump(new_entry)
    return jsonify({"data": result.data})


class EntryList(Resource):
  def get(self):
    user_entries = Entry.query.filter_by(user_id=session['user_id']).all()
    result = entries_schema.dump(user_entries)
    return jsonify({"data": result.data})

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

api.add_resource(EntryResource, '/entries')
api.add_resource(EntryList, '/entries')
api.add_resource(TypeList, '/types', )