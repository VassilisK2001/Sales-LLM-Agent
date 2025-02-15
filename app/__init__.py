from flask import Flask
from config import constants
from app.routes import configure_routes 


def create_app():
    app = Flask(__name__)
    app.secret_key = constants.FLASK_SECRET_KEY 

    configure_routes(app)

    return app