from app import ma
from models import (
  User,
  Entry
)

class UserSchema(ma.ModelSchema):
  class Meta:
    model = User

class EntrySchema(ma.ModelSchema):
  class Meta:
    model = Entry