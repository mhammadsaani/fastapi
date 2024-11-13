import psycopg2
from config import DB_USER, DB_PASSWORD, DB_HOST, DB_PORT, DB_NAME
import random


def create_db_connection():
    conn = psycopg2.connect(
        user=DB_USER,
        password=DB_PASSWORD,
        host=DB_HOST,
        port=DB_PORT,
        database=DB_NAME
    )
    conn.autocommit = True
    print("Database connection successful")
    return conn


def mimic_model():
    return random.randint(10, 100)