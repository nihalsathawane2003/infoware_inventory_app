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

from PySide6.QtWidgets import QWidget, QFormLayout, QLineEdit, QPushButton, QVBoxLayout, QLabel

class SalesUI(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Sales")
        self.setGeometry(100, 100, 400, 400)

        layout = QFormLayout()
        layout.addRow("Customer:", QLineEdit())
        layout.addRow("Product:", QLineEdit())
        layout.addRow("Quantity:", QLineEdit())
        layout.addRow("Rate per Unit:", QLineEdit())
        layout.addRow("GST %:", QLineEdit())
        layout.addRow(QPushButton("Record Sale"))

        container = QVBoxLayout()
        container.addLayout(layout)
        self.setLayout(container)

