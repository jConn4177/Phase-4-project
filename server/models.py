from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData, Enum
from sqlalchemy.orm import validates
from flask_bcrypt import Bcrypt, generate_password_hash, check_password_hash

convention = {
    "ix": "ix_%(column_0_label)s",
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(constraint_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s",
}

metadata = MetaData(naming_convention=convention)

db = SQLAlchemy(metadata=metadata)
bcrypt = Bcrypt()


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(41), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128))
    is_seller = db.Column(db.Boolean, default=False)
    cart_items = db.relationship('Cart', backref='user', lazy=True)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "is_seller": self.is_seller
        }

    @validates('name')
    def validate_name(self, key, name):
        if not isinstance(name, str):
            raise AssertionError('Name must be a string')
        if len(name) < 2:
            raise AssertionError('Name must be at least two characters long')
        return name

    @validates('email')
    def validate_email(self, key, email):
        if not isinstance(email, str):
            raise AssertionError('Email must be a string')
        if len(email) < 5:
            raise AssertionError('Email must be at least five characters long')
        return email

    def set_password(self, password):
        self.password_hash = bcrypt.generate_password_hash(
            password).decode('utf-8')

    def check_password(self, password):
        return bcrypt.check_password_hash(self.password_hash, password)


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(255))
    price = db.Column(db.Float, nullable=False)
    image = db.Column(db.String(255))  # You can store the image path
    count = db.Column(db.Integer, nullable=False)
    category = db.Column(Enum('Aviator', 'Wayfarer', 'Round',
                         'Sports', 'Designer', 'Oversized', 'Cat-Eye'), nullable=True)
    cart_items = db.relationship('Cart', backref='product', lazy=True)


class Cart(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # 'users.id' instead of 'user.id'
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey(
        'product.id'), nullable=False)
    quantity = db.Column(db.Integer, default=1)
