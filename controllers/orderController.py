from flask import request, jsonify
from models.schemas.orderSchema import order_schema, orders_schema
from services import orderService
from marshmallow import ValidationError
from caching import cache


def save():
    
    try:
        
        order_data = order_schema.load(request.json)
        
    except ValidationError as e:
        return jsonify(e.messages), 400
    
    order_saved = orderService.save(order_data)
    return order_schema.jsonify(order_data), 201

@cache.cached(timeout=60)
def find_all():
    all_orders = orderService.find_all()
    return orders_schema.jsonify(all_orders), 200

def find_all_paginate():
    page = int(request.args.get("page"))
    per_page = int(request.args.get("per_page"))
    orders = orderService.find_all_paginate(page, per_page)
    return orders_schema.jsonify(orders), 200