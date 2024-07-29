from . import ma
from marshmallow import fields, Schema, validate

class ProductSchema(ma.Schema):
    id = fields.Integer(required=False)
    name = fields.String(required=False)
    price = fields.Float(required=False)
    
    class Meta:
        fields = ("id", "name", "price")
        
        
product_schema = ProductSchema()
products_schema = ProductSchema(many=True)
