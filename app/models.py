from app import db

from datetime import datetime

class User(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
  updated_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

class Entry(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  text = db.Column(db.String(80), nullable=False)
  type = db.Column(db.String(80), nullable=False)
  active_after = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
  created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
  updated_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
  user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
  entry_generator_id = db.Column(db.Integer, db.ForeignKey('entry_generator.id'), nullable=True)
  show_before_active = db.Column(db.Boolean, nullable=False, default=False)

  def __repr__(self):
    return '<Entry %r>' % self.text

class EntryGenerator(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  entry_text = db.Column(db.String(80), nullable=False)
  entry_type = db.Column(db.String(80), nullable=False)
  repeat_frequency = db.Column(db.String(80), nullable=False)
  start_at = db.Column(db.Integer, nullable=False, default=1)
  user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
  created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
  updated_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

  def __repr__(self):
    return '<EntryGenerator %r>' % self.entry_text
  
class Note(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  entry_id = db.Column(db.Integer, db.ForeignKey('entry.id'), nullable=False)
  text = db.Column(db.Text, nullable=False)
  created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
  updated_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

  def __repr__(self):
    return '<Note %r>' % self.text

class Status(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
  status_text = db.Column(db.String(80), nullable=False)
  created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
  updated_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

  def __repr__(self):
    return '<Status %r>' % self.status_text