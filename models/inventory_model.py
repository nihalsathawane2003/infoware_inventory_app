from db.db_config import get_connection

def create_inventory_table():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS inventory (
            product_id INT PRIMARY KEY,
            quantity DECIMAL(10,2) DEFAULT 0,
            min_stock DECIMAL(10,2) DEFAULT 0,
            max_sale_unit DECIMAL(10,2) DEFAULT 0,
            FOREIGN KEY (product_id) REFERENCES products(id)
        )
    """)
    conn.commit()
    conn.close()

def validate_stock(product_id, sale_qty):
    conn = get_connection()
    cur = conn.cursor(dictionary=True)
    cur.execute("SELECT quantity, max_sale_unit FROM inventory WHERE product_id = %s", (product_id,))
    row = cur.fetchone()
    conn.close()
    if row:
        if sale_qty > row['quantity']:
            return False, "Not enough stock"
        if row['max_sale_unit'] and sale_qty > row['max_sale_unit']:
            return False, "Exceeds max saleable quantity"
    return True, "OK"

def get_inventory():
    conn = get_connection()
    cur = conn.cursor(dictionary=True)
    cur.execute("""
        SELECT p.name, i.quantity, i.min_stock, i.max_sale_unit
        FROM inventory i
        JOIN products p ON i.product_id = p.id
    """)
    rows = cur.fetchall()
    conn.close()
    return rows
