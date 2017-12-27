from app import ma
from marshmallow import fields
from models import (
  User,
  Entry,
  Type
)

class UserSchema(ma.ModelSchema):
  class Meta:
    model = User

class EntrySchema(ma.ModelSchema):
  class Meta:
    model = Entry
    ordered = True

class TypeSchema(ma.ModelSchema):
  entries = ma.Nested(EntrySchema, many=True)

  class Meta:
    model = Type