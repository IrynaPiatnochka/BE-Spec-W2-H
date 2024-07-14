from . import ma
from marshmallow import fields

class CustomerSchema(ma.Schema):
    id = fields.Integer(required=False)
    name = fields.String(required=False)
    email = fields.Email(required=False)
    phone = fields.String(required=False)
    username = fields.String(required=False)
    password = fields.String(required=False)
    
    class Meta:
        fields = ("id", "name", "email", "phone", "username", "password")
        
        
customer_schema = CustomerSchema()
customers_schema = CustomerSchema(many=True, exclude=["password"])
