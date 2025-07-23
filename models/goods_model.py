from PySide6.QtWidgets import (
    QWidget, QFormLayout, QLineEdit, QPushButton, QVBoxLayout,
    QLabel, QComboBox, QMessageBox
)
from PySide6.QtCore import Qt
from db.db_config import receive_goods  


class GoodsReceivingUI(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Goods Receiving")
        self.setGeometry(100, 100, 400, 500)

        layout = QFormLayout()

        self.product = QComboBox()
        self.unit = QComboBox()
        self.quantity = QLineEdit()
        self.rate = QLineEdit()
        self.gst = QLineEdit()
        self.total = QLabel("0.00")

        self.product.addItems(["", "Apples", "Bananas", "Oranges"])
        self.unit.addItems(["", "Kg", "Liters", "Units"])

        self.submit_button = QPushButton("Receive Goods")
        self.submit_button.clicked.connect(self.submit_goods)

        layout.addRow("Product:", self.product)
        layout.addRow("Unit:", self.unit)
        layout.addRow("Quantity:", self.quantity)
        layout.addRow("Rate per Unit:", self.rate)
        layout.addRow("GST %:", self.gst)
        layout.addRow("Total Amount:", self.total)
        layout.addRow(self.submit_button)

        container = QVBoxLayout()
        container.addLayout(layout)
        self.setLayout(container)

    def submit_goods(self):
        if self.product.currentText().strip() == "":
            QMessageBox.warning(self, "Input Error", "Please select a product.")
            return

        if self.unit.currentText().strip() == "":
            QMessageBox.warning(self, "Input Error", "Please select a unit.")
            return

        try:
            quantity = float(self.quantity.text().strip())
            rate = float(self.rate.text().strip())
            gst = float(self.gst.text().strip())
        except ValueError:
            QMessageBox.warning(self, "Input Error", "Quantity, Rate, and GST must be numbers.")
            return

        total_amount = quantity * rate
        total_with_gst = total_amount + (total_amount * gst / 100)
        self.total.setText(f"{total_with_gst:.2f}")

        product_map = {
            "Apples": 1,
            "Bananas": 2,
            "Oranges": 3
        }

        product_name = self.product.currentText().strip()
        product_id = product_map.get(product_name)

        if not product_id:
            QMessageBox.warning(self, "Error", "Product not mapped in code.")
            return

        data = {
            'product_id': product_id,
            'quantity': quantity,
            'unit': self.unit.currentText().strip(),
            'rate': rate,
            'gst': gst
        }

        try:
            receive_goods(data)
            QMessageBox.information(self, "Success", "Goods received and stored in DB!")
        except Exception as e:
            QMessageBox.critical(self, "DB Error", f"Failed to insert into DB: {e}")
