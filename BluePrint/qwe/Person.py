from flask import Blueprint

api = Blueprint("zxc", __name__, url_prefix="/user")

@api.route('/center')
def center():
    return 'center'

@api.route('/Young')
def Young():
    return 'Hello Young!'