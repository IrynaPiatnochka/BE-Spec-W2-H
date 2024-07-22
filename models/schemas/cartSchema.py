from models.cart import Cart
from . import ma
from marshmallow import fields, Schema


class CartSchema(ma.Schema):

    id = fields.Integer(required=False)
    customer_id = fields.Integer(required=True, nullable=False)
    product_id = fields.Integer(required=True, nullable=False)
    quantity = fields.Integer(required=True, nullable=False)
    # product = fields.Nested("ProductSchema", many=True)
    
# class CartReturnSchema(ma.SQLAlchemySchema):
#     class Meta():
#         model = Cart
#         fields = ("id" )
#         products = fields.Nested("ProductSchema", many=True)
    

    # id = fields.Integer(required=False)
    # product_name = fields.String(required=True, nullable=False)
    # product_price = fields.Float(required=True, nullable=False)
    # product_quantity = fields.Integer(required=True, nullable=False)
    
    

cart_schema = CartSchema(many=True)
carts_schema = CartSchema(many=True)
# cart_return_schema = CartReturnSchema(many=True)