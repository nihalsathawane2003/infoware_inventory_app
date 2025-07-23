from db.db_config import get_connection
from models.inventory_model import validate_stock

def create_sales_table():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS sales (
            id INT AUTO_INCREMENT PRIMARY KEY,
            product_id INT,
            customer VARCHAR(100),
            quantity DECIMAL(10,2),
            unit VARCHAR(50),
            rate_per_unit DECIMAL(10,2),
            gst_tax DECIMAL(5,2),
            total_amount DECIMAL(10,2),
            FOREIGN KEY (product_id) REFERENCES products(id)
        )
    """)
    conn.commit()
    conn.close()

def record_sale(data):
    valid, message = validate_stock(data['product_id'], data['quantity'])
    if not valid:
        return False, message

    conn = get_connection()
    cur = conn.cursor()
    total = data['quantity'] * data['rate']
    cur.execute("""
        INSERT INTO sales
        (product_id, customer, quantity, unit, rate_per_unit, gst_tax, total_amount)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
    """, (
        data['product_id'], data['customer'], data['quantity'], data['unit'],
        data['rate'], data['gst'], total
    ))
    conn.commit()

    cur.execute("UPDATE inventory SET quantity = quantity - %s WHERE product_id = %s",
                (data['quantity'], data['product_id']))
    conn.commit()
    conn.close()

    return True, "Sale recorded successfully"
