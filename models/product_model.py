from db.db_config import get_connection

def create_product_table():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS products (
            id INT PRIMARY KEY AUTO_INCREMENT,
            barcode VARCHAR(255),
            sku_id VARCHAR(255),
            category VARCHAR(255),
            subcategory VARCHAR(255),
            image_path VARCHAR(255),
            name VARCHAR(255),
            description TEXT,
            gst_tax FLOAT,
            price FLOAT,
            default_unit VARCHAR(255),
            conversion_factor FLOAT,
            supplier_id INT,
            gst FLOAT
        )
    """)
    conn.commit()
    conn.close()

def add_product(data):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        INSERT INTO products 
        (barcode, sku_id, name, category, subcategory, gst_tax, price, 
         default_unit, conversion_factor, supplier_id, image_path, description, gst)
        VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
    """, (
        data['barcode'], data['sku_id'], data['name'], data['category'],
        data['subcategory'], data['gst_tax'], data['price'], data['default_unit'],
        data['conversion_factor'], data['supplier_id'], data['image_path'],
        data['description'], data['gst']
    ))
    conn.commit()
    last_id = cur.lastrowid
    conn.close()
    return last_id

def get_all_products():
    conn = get_connection()
    cur = conn.cursor(dictionary=True)
    cur.execute("SELECT * FROM products")
    rows = cur.fetchall()
    conn.close()
    return rows
