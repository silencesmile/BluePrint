from flask import Blueprint

shop = Blueprint("shop", __name__)

@shop.route('/goods')
def goods():
    return 'Hello goods!'

@shop.route('/orders')
def orders():
    return 'Hello orders!'

@shop.route('/shopping')
def shopping():
    return 'Hello shopping!'