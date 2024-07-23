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


def remove_from_cart():
    data = request.get_json()
    customer_id = data.get('customer_id')
    product_id = data.get('product_id')

    if not customer_id and not product_id:
        return jsonify({'error': 'Customer ID and Product ID are required'}), 400
    result = remove_from_cart( product_id)
    return jsonify(result)


def empty_cart(id):
    try:
        success = cartService.empty_cart(id)
        if success:
            return jsonify({"message": "Cart emptied successfully"}), 200
        else:
            return jsonify({"message": "Cart not found"}), 404
    except ValidationError as e:
        return jsonify(e.messages), 400
    