from flask import Flask
from api.handlers.tokens import add_token
from api.handlers.bill import create_bill


def setup_routes(app: Flask):
    app.add_url_rule('/token', 'add_token', add_token, methods=['POST'])
    app.add_url_rule('/bill', 'create_bill', create_bill, methods=['PUT'])


def get_app():
    app = Flask(__name__)
    setup_routes(app)
    return app
