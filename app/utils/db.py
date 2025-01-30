import mysql.connector
from app.utils.config import config
import os

# MySQL database configuration
db_config = {
    "host": config.DB_HOST,
    "user": config.DB_USER,
    "password": config.DB_PASSWORD,
    "database": config.DB_NAME,
}


def get_db_connection():
    return mysql.connector.connect(**db_config)
