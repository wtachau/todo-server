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
  created_at = ma.DateTime('%Y-%m-%d')
  updated_at = ma.DateTime('%Y-%m-%d')
  active_after = ma.DateTime('%Y-%m-%d')

  class Meta:
    model = Entry
    additional = ('active_after',)
    # exclude = ('type', )
    ordered = True

class TypeSchema(ma.ModelSchema):
  entries = ma.Nested(EntrySchema, many=True)

  class Meta:
    model = Type