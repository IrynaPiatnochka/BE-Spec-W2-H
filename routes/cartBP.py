from flask import Blueprint
from controllers.cartController import view_cart, empty_cart
from services.cartService import add_to_cart, remove_from_cart


cart_blueprint = Blueprint('cart_bp', __name__)


cart_blueprint.route('/add_to_cart', methods=['POST'])(add_to_cart)
cart_blueprint.route('/<int:customer_id>', methods=['GET'])(view_cart)
cart_blueprint.route('/remove_item/<customer_id>/<product_id>', methods=['DELETE'])(remove_from_cart)
cart_blueprint.route('/delete/<int:id>', methods=['DELETE'])(empty_cart)


