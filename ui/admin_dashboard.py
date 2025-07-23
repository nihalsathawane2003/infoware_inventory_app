from PySide6.QtWidgets import QWidget, QVBoxLayout, QPushButton
from ui.product_form import ProductForm

class AdminDashboard(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        prod_btn = QPushButton("Product Master")
        prod_btn.clicked.connect(self.open_product)
        layout.addWidget(prod_btn)

        self.setLayout(layout)

    def open_product(self):
        self.pw = ProductForm()
        self.pw.show()
