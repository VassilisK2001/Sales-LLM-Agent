from flask import Flask
from config import constants


def create_app():
    app = Flask(__name__)
    app.secret_key = constants.FLASK_SECRET_KEY 

    from app.routes import configure_routes 
    configure_routes(app)

    return app