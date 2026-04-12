# Add any model classes for Flask-SQLAlchemy here
from app import db

class Movie (db.Model):
    __tablename__ = 'movies'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(128))
    description = db.Column(db.Text(255))
    poster = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.Timestamptz)

def __init__(self, title, description, poster,created_at):
    super().__init__()
    self.title = title
    self.description = description
    self.poster = poster
    self.created_at = created_at