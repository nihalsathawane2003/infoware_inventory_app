from config import DB_CONFIG
import mysql.connector
from db.db_config import get_connection

def get_user_by_username(username):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM users WHERE username = %s", (username,))
    user = cursor.fetchone()
    conn.close()
    return user

def verify_user(username, password, role):
    # Simulated DB check
    if username == "admin" and password == "123" and role == "Admin":
        return {"username": username, "role": role}
    elif username == "operator" and password == "456" and role == "Operator":
        return {"username": username, "role": role}
    return None

def create_users_table():
    conn = mysql.connector.connect(**DB_CONFIG)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INT AUTO_INCREMENT PRIMARY KEY,
            username VARCHAR(255) UNIQUE NOT NULL,
            password VARCHAR(255) NOT NULL,
            role ENUM('Admin', 'Operator') NOT NULL
        )
    """)
    
def add_user(username, password, role):
    # Check if user already exists
    if get_user_by_username(username):
        return False  # Username taken

    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO users (username, password, role) VALUES (%s, %s, %s)",
        (username, password, role)
    )
    conn.commit()
    conn.close()
    return True


