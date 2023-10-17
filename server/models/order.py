
from server import db
from server.models.serializers import SerializableMixin


class Order(db.Model, SerializableMixin):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    user = db.relationship('User', backref='orders')
    # Add other fields like order date, status, etc.

    def serialize(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            # Add other fields as needed
        }
