from flask import request, jsonify
from models.schemas.customerSchema import customer_schema, customers_schema
from services import customerService
from marshmallow import ValidationError
from caching import cache


def save():
    
    try:
        
        customer_data = customer_schema.load(request.json)
        
    except ValidationError as e:
        return jsonify(e.messages), 400
    
    customer_saved = customerService.save(customer_data)
    return customer_schema.jsonify(customer_data), 201

@cache.cached(timeout=60)
def find_all():
    all_customers = customerService.find_all()
    return customers_schema.jsonify(all_customers), 200
