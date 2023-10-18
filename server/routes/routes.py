from flask import Blueprint, jsonify, request
from server.models.product import Product
from server.app import db

routes = Blueprint('routes', __name__)


@app.route('/')
def index():
    return '<h1>Code challenge</h1>'


@routes.route('/products', methods=['GET'])
def get_products():
    products = Product.query.all()
    return jsonify([product.serialize() for product in products])


@routes.route('/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    product = Product.query.get(product_id)
    if not product:
        return jsonify(message="Product not found"), 404
    return jsonify(product.serialize())


@routes.route('/products', methods=['POST'])
def create_product():
    data = request.get_json()
    product = Product(**data)
    db.session.add(product)
    db.session.commit()
    return jsonify(message="Product created successfully", product=product.serialize()), 201


@routes.route('/products/<int:product_id>', methods=['PUT'])
def update_product(product_id):
    data = request.get_json()
    product = Product.query.get(product_id)
    if not product:
        return jsonify(message="Product not found"), 404
    for key, value in data.items():
        setattr(product, key, value)
    db.session.commit()
    return jsonify(message="Product updated successfully", product=product.serialize())


@routes.route('/products/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    product = Product.query.get(product_id)
    if not product:
        return jsonify(message="Product not found"), 404
    db.session.delete(product)
    db.session.commit()
    return jsonify(message="Product deleted successfully"), 204
