import pymysql

DATABASE_CONFIG = {
    "host": "localhost",
    "user": "root",
    "password": "0522",
    "database": "pas",
}

def get_connection():
    return pymysql.connect(**DATABASE_CONFIG)
