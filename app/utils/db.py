import mysql.connector
import os

# MySQL database configuration
db_config = {
    # "host": "localhost",  # Use "db" for Docker Compose
    # "user": "dbroot",
    # "password": "root",
    # "database": "py_sample",
    "host": os.getenv("DB_HOST"),
    "user": os.getenv("DB_USER"),
    "password": os.getenv("DB_PASSWORD"),
    "database": os.getenv("DB_NAME"),
}


def get_db_connection():
    return mysql.connector.connect(**db_config)