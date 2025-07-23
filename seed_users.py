from werkzeug.security import generate_password_hash
import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="nihal",
    database="infowaredb"
)

cursor = conn.cursor()

from werkzeug.security import generate_password_hash

users = [
    ("admin", generate_password_hash("admin123"), "admin"),
    ("operator", generate_password_hash("operator123"), "operator")
]

for username, password, role in users:
    cursor.execute("""
        INSERT INTO users (username, password, role)
        VALUES (%s, %s, %s)
        ON DUPLICATE KEY UPDATE username = username;
    """, (username, password, role))

conn.commit()
cursor.close()
conn.close()

print("✅ Hashed passwords inserted.")
