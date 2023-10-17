from server import db
from server.models.serializers import SerializableMixin

product_categories = db.Table(
    'product_categories',
    db.Column('product_id', db.Integer, db.ForeignKey(
        'product.id'), primary_key=True),
    db.Column('category_id', db.Integer, db.ForeignKey(
        'category.id'), primary_key=True)
)


class Product(db.Model, SerializableMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=True)
    price = db.Column(db.Float, nullable=False)
    sold_out = db.Column(db.Boolean, nullable=False)

    categories = db.relationship(
        'Category', secondary=product_categories, backref=db.backref('products', lazy='dynamic'))

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'price': self.price,
            'sold_out': self.sold_out,
            'categories': [category.name for category in self.categories],
        }
