from server import db
from server.models.serializers import SerializableMixin


class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(41), nullable=False, unique=True)
