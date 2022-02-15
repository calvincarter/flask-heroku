from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def connect_db(app):
  db.app = app
  db.init_app(app)

class Pet(db.Model):
  __tablename__ = 'pets'
  id = db.Column(db.Integer, primary_key=True, autoincrement=True)
  name = db.Column(db.String(255))

  def to_json(self):
    return {
        "id": int(self.id),
        "name": self.name,
    }