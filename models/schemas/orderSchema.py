from . import ma
from marshmallow import fields

class OrderSchema(ma.Schema):
    id = fields.Integer(required=False)
    order_date = fields.Date(required=False)
    customer_id = fields.Integer(required=True)
    products = fields.Nested("ProductSchema", many=True)
    customer = fields.Nested("CustomerOrderSchema")

    class Meta:
        fields = ("id", "order_date", "customer_id", 'product_ids', 'products', 'customer')  

order_schema = OrderSchema()
orders_schema = OrderSchema(many=True)


