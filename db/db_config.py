import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="nihal",
        database="infowaredb"
    )

def receive_goods(data):
    try:
        conn = get_connection()
        cur = conn.cursor()

        subtotal = data['quantity'] * data['rate_per_unit']
        total_with_gst = subtotal + (subtotal * data['gst_tax'] / 100)

        cur.execute("""
            INSERT INTO goods_receiving (
                product_id, quantity, unit, rate_per_unit, gst_tax, total_amount
            ) VALUES (%s, %s, %s, %s, %s, %s)
        """, (
            data['product_id'],
            data['quantity'],
            data['unit'],
            data['rate_per_unit'],
            data['gst_tax'],
            total_with_gst
        ))

        conn.commit()
        conn.close()

    except Exception as e:
        raise Exception(f"MySQL error: {e}")
