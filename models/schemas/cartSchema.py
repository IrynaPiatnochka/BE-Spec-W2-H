from models.cart import Cart
from . import ma
from marshmallow import fields, Schema


class CartSchema(ma.Schema):

    id = fields.Integer(required=False)
    customer_id = fields.Integer(required=True, nullable=False)
    product_id = fields.Integer(required=True, nullable=False)
    quantity = fields.Integer(required=True, nullable=False)
  
    
cart_schema = CartSchema()
carts_schema = CartSchema(many=True)
