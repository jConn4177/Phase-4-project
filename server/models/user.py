from app import db
from server.models.serializers import SerializableMixin


class User(db.Model, SerializableMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(23), unique=True, nullable=False)
    password = db.Column(db.String(23), nullable=False)
    name = db.Column(db.String(41), nullable=False)
    address = db.Column(db.String(255))
    seller = db.Column(db.Boolean, nullable=False, default=False)
    cart_id = db.Column(db.Integer, db.ForeignKey("cart.id"))

    def serialize(self):
        return {
            'id': self.id,
            'email': self.email,
            'password': self.password,
            'name': self.name,
            'address': self.address,
            'seller': self.seller,
            'cart_id': self.cart_id
        }
