from database import db
from models.order import Order
from sqlalchemy import select
from datetime import date
from models.product import Product
from models.customer import Customer
from models.cart import Cart
from models.order_product import order_product
from services.cartService import empty_cart
from flask import jsonify, request


# def save(order_data):
    
#     new_order = Order(order_date=date.today(), customer_id=order_data['customer_id'])
#     cart = []
    
#     for item_id in cart:
#         query = select(Product).filter(Product.name == item_id)
#         item = db.session.execute(query).scalar()
#         new_order.products.append(item)
    
#     db.session.add(new_order)
#     db.session.commit()
    
#     db.session.refresh(new_order)
#     return new_order

def save_order():

    new_order = Order(order_date=date.today(), customer_id=request.json['customer_id'])
    customer_id=request.json['customer_id']
    cart = []
    for item_id in cart:
        query = select(Product).filter(Product.name == item_id)
        item = db.session.execute(query).scalar()
        new_order.products.append(item)
        
    db.session.add(new_order)
    db.session.commit()
    empty_cart(customer_id)
    return {'message': 'Order placed successfully'}, 200


def checkout():
    result = save_order()
    return jsonify(result)


def find_all():
    query = select(Order)
    all_orders = db.session.execute(query).scalars().all()
    return all_orders

# def find_by_id(id):
#     query = select(Order).filter(Order.id==id)
#     orders = db.session.execute(query).scalars().all()
#     return orders

# def find_by_customer_id(id):
#     query = select(Order).filter(Order.customer_id==id)
#     orders = db.session.execute(query).scalars().all()
#     return orders

def find_by_customer_email(email):
    query = select(Order).join(Customer).where(Customer.id==Order.customer_id).filter(Customer.email == email)
    orders = db.session.execute(query).scalars().all()
    return orders

def find_all_paginate(page, per_page):
    query = select(Order)
    orders = db.paginate(query, page=page, per_page=per_page)
    return orders


