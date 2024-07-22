from database import db
from models.cart import Cart
from models.product import Product
from models.customer import Customer
from sqlalchemy import select, delete
from sqlalchemy.sql import text




def view_cart(customer_id):
    # search_cart = db.session.query(Cart.id, Product.name, Product.price, Cart.quantity).filter(Product.id == Cart.product_id).filter(Cart.customer_id == customer_id)
    # query = select(Cart).filter(Cart.customer_id == customer_id)
    search_cart = db.session.query(Cart).filter(Cart.customer_id == customer_id).all()
    sql = """
    select ecom_db.cart.id,
    ecom_db.products.name
    # ecom_db.products.price
    # ecom_db.cart.quantity 
    from ecom_db.cart
    join ecom_db.products on ecom_db.products.id = ecom_db.cart.product_id
    where ecom_db.cart.customer_id = """ + str(customer_id)
    
    # search_cart = db.session.execute(text(sql)).all()
    
    
    # search_cart = db.session.execute(query).all()
    # search_cart = db.session.execute(text(sql)).all()
    print(search_cart)
    return search_cart
    
    
    # cart_entries = Cart.query.filter(Cart.customer_id == customer_id).all()
    # cart_data = [{'product_id': entry.product_id, 'quantity': entry.quantity} for entry in cart_entries]
    # return cart_data, 200


def add_to_cart(cart_data):
    new_cart = Cart(customer_id=cart_data['customer_id'], 
                    product_id=cart_data['product_id'],
                    quantity=cart_data['quantity'])
    
    db.session.add(new_cart)
    db.session.commit()
    
    db.session.refresh(new_cart)
    return new_cart


def remove_from_cart(customer_id, product_id):
    cart_entry = Cart.query.filter(customer_id=customer_id, product_id=product_id).first()
    if cart_entry:
        db.session.delete(cart_entry)
        db.session.commit()
        return {'message': 'Product removed from cart successfully'}, 200
    else:
        return {'error': 'Product not found in cart'}, 404
    

def empty_cart(customer_id):
    cart_entries = Cart.query.filter(customer_id=customer_id).all()
    for entry in cart_entries:
        db.session.delete(entry)
    db.session.commit()
    return {'message': 'Cart emptied successfully'}, 200


