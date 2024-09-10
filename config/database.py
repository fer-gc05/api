import pymysql
import os

DATABASE_CONFIG = {
    "host": os.getenv("DB_HOST"),
    "user": os.getenv("DB_USER"),
    "password": os.getenv("DB_PASSWORD"),
    "database": os.getenv("DB_NAME"),
}

def get_connection():
    try:
        connection = pymysql.connect(**DATABASE_CONFIG)
        return connection
    except pymysql.MySQLError as e:
        print(f"Error connecting to MySQL database: {e}")
        return None
