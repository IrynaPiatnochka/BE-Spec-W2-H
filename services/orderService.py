from database import db
from models.order import Order
from sqlalchemy import select
from datetime import date
from models.product import Product
from models.customer import Customer

def save(order_data):
    
    new_order = Order(order_date=order_data['order_date'], customer_id=order_data['customer_id'])
    
    db.session.add(new_order)
    db.session.commit()
    
    db.session.refresh(new_order)
    return new_order

def find_all():
    query = select(Order)
    all_orders = db.session.execute(query).scalars().all()
    return all_orders

def find_all_paginate(page, per_page):
    query = select(Order)
    orders = db.paginate(query, page=page, per_page=per_page)
    return orders