from database import db
from models.cart import Cart
from models.product import Product
from models.customer import Customer
from sqlalchemy import delete
from flask import request
from models.schemas.cartSchema import carts_schema
from models.schemas.productSchema import products_schema

from models.schemas import cartSchema, productSchema


# def view_cart(customer_id):
#     search_cart = db.session.query(Cart).filter(Cart.customer_id == customer_id).all()
    
#     products=db.session.query(Product).filter(Cart.product_id == request.json['product_id']).all()
#     print(search_cart, products)
#     return search_cart
    
def view_cart(customer_id):
    cart_items = db.session.query(Cart, Product).join(Product, Cart.product_id == Product.id).filter(Cart.customer_id == customer_id).all()
  
    result = []
    for cart, product in cart_items:
        item = {
            "cart_id": cart.id,
            "customer_id": cart.customer_id,
            "product_id": cart.product_id,
            "quantity": cart.quantity,
            "product": {
                "name": product.name,
                "price": product.price
            }
        }
        result.append(item)
        
    print(result)
    return result

def add_to_cart():
    new_cart = Cart(customer_id=request.json['customer_id'], product_id=request.json['product_id'], quantity=request.json['quantity'])
    if new_cart:
        db.session.add(new_cart)
        db.session.commit()
        return {'message': 'Product added to cart successfully'}, 200
    else:
        return {'error': 'Product not found in cart'}, 404


def remove_from_cart(customer_id, product_id):
    query = delete(Cart).filter(Cart.customer_id == customer_id, Cart.product_id==product_id )
    db.session.execute(query)
    db.session.commit()
    return {'message': 'Product removed from cart successfully'}, 200

    
def empty_cart(customer_id):
    query = delete(Cart).filter(Cart.customer_id == customer_id)
    db.session.execute(query)
    db.session.commit()
    return {'message': 'Cart emptied successfully'}, 200


