import mysql.connector
from dotenv import load_dotenv
import os

load_dotenv()

def get_db_connection():
    return mysql.connector.connect(
        host=os.getenv('DB_HOST'),
        user=os.getenv('DB_USERNAME'),
        password=os.getenv('DB_PASSWORD'),
        database=os.getenv('DB_NAME')
    )

def save_prediction_to_db(prediction_id, result_integer, phase, confidence_score, created_at):
    connection = get_db_connection()
    cursor = connection.cursor()
    query = """
        INSERT INTO predictions (id, result, phase, confidence_score, created_at)
        VALUES (%s, %s, %s, %s, %s)
    """
    cursor.execute(query, (prediction_id, result_integer, phase, confidence_score, created_at))
    connection.commit()
    cursor.close()
    connection.close()
