from flask import request, jsonify
from models.schemas.cartSchema import cart_schema
from services import cartService
from models.product import Product
from models.cart import Cart
from marshmallow import ValidationError
from caching import cache
from database import db


def view_cart(customer_id):
    cart = cartService.view_cart(customer_id)
    print(cart)
    return cart_schema.jsonify(cart)


def add_to_cart():
    try:
        cart_data = cart_schema.load(request.json)
    except ValidationError as e:
        return jsonify(e.messages), 400
    
    cart_saved = cartService.add_to_cart(cart_data)
    return cart_schema.jsonify(cart_data), 201
    
    
    try:
        cart_data = cart_schema.load(request.json)
    except ValidationError as e:
        return jsonify(e.messages), 400

    customer_id = cart_data.get('customer_id')
    product_id = cart_data.get('product_id')
    quantity = cart_data.get('quantity', 1)  

    product = Product.db.session.query.get(product_id)
    if not product:
        return jsonify({'error': 'Product not found'}), 404

    cart_entry = cartService.add_to_cart(cart_data)

    return cart_schema.jsonify(cart_entry), 201  

def remove_from_cart():
    data = request.get_json()
    product_id = data.get('product_id')

    if not product_id:
        return jsonify({'error': 'Product ID is required'}), 400

    result = remove_from_cart(product_id)
    return jsonify(result)


def empty_cart(customer_id):
    try:
        result = empty_cart(customer_id)
        return jsonify(result)
    except Exception as e:
        return jsonify({'error': str(e)}), 500