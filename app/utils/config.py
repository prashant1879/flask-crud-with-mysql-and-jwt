# config.py
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file
import os


class Config:
    # DATABASE_URI = os.getenv("DATABASE_URI", "default_database_uri")
    # API_KEY = os.getenv("API_KEY", "default_api_key")
    DEBUG = os.getenv("DEBUG", "False").lower() == "true"


class DevelopmentConfig(Config):
    DEBUG = True
    # API keys
    SECRET_KEY = "a3360acf702efaa1c31d33661ef73e0c93059ed92def6f1b6620c848078ce59a"
    JWT_SECRET_KEY = "0ff4506e0fef5b086ae086eea39e3d2fb4e377cc69a0356482e237f1ddabf898"
    DB_HOST = "localhost"
    DB_USER = "dbroot"
    DB_PASSWORD = "root"
    DB_NAME = "py_sample"
    MODEL = "DEV"


class ProductionConfig(Config):
    DEBUG = False
    # API keys
    SECRET_KEY = "a3360acf702efaa1c31d33661ef73e0c93059ed92def6f1b6620c848078ce59a"
    JWT_SECRET_KEY = "0ff4506e0fef5b086ae086eea39e3d2fb4e377cc69a0356482e237f1ddabf898"
    DB_HOST = "localhost"
    DB_USER = "dbroot"
    DB_PASSWORD = "root"
    DB_NAME = "py_sample"
    MODEL = "PROD"


# Select the appropriate configuration
if os.getenv("ENVIRONMENT") == "development":
    config = DevelopmentConfig()  # or TestingConfig()
else:
    config = ProductionConfig()
