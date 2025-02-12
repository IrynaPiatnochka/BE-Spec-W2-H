from flask import Flask
from database import db
from models.schemas import ma
from flask_swagger_ui import get_swaggerui_blueprint

from models.customer import Customer
from routes.customerBP import customer_blueprint

from models.product import Product
from routes.productBP import product_blueprint

from models.order import Order
from routes.orderBP import order_blueprint

from models.order_product import order_product

from models.cart import Cart
from routes.cartBP import cart_blueprint


from limiter import limiter
from caching import cache


SWAGGER_URL = '/api/docs' 
API_URL = '/static/swagger.yaml'

swagger_blueprint = get_swaggerui_blueprint(SWAGGER_URL, API_URL, config={'app_name': 'E-Commerce API'})


def create_app(config_name):
    
    app = Flask(__name__)
    
    app.config.from_object(f'config.{config_name}')
    db.init_app(app)
    
    ma.init_app(app)
    # limiter.init_app(app)
    cache.init_app(app)
    
    return app

def blueprint_config(app):
    app.register_blueprint(customer_blueprint, url_prefix='/customers')
    app.register_blueprint(product_blueprint, url_prefix='/products')
    app.register_blueprint(order_blueprint, url_prefix='/orders')
    app.register_blueprint(cart_blueprint, url_prefix='/cart')
    app.register_blueprint(swagger_blueprint, url_prefix=SWAGGER_URL)
    
def rate_limit_config():
    limiter.limit("200 per day")(customer_blueprint)

if __name__ == '__main__':
    app = create_app('DevelopmentConfig')
    
    blueprint_config(app)
    
    rate_limit_config()
    
    with app.app_context():
        # db.drop_all()
        db.create_all()
    
    app.run()