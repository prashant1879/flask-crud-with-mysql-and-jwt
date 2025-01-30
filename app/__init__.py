from flask import Flask
from flask_jwt_extended import JWTManager
from app.utils.config import config
from dotenv import load_dotenv


load_dotenv()  # Load environment variables from .env file

from app.views.employee_view import employee_bp


def create_app():
    app = Flask(__name__)

    # Set Flask configuration from environment variables
    app.config["SECRET_KEY"] = config.SECRET_KEY
    app.config["JWT_SECRET_KEY"] = config.JWT_SECRET_KEY
    app.config["JWT_TOKEN_LOCATION"] = ["headers"]  # Look for JWT in headers

    # Initialize JWT
    jwt = JWTManager(app)

    app.register_blueprint(employee_bp, url_prefix="/api")
    return app
