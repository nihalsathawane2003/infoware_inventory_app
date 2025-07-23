# ui/operator_dashboard.py

from PySide6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLabel
from PySide6.QtCore import Qt

from ui.goods_receiving_ui import GoodsReceivingUI
from ui.sales_ui import SalesUI
from ui.inventory_view_ui import InventoryViewUI

class OperatorDashboard(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Operator Dashboard")
        layout = QVBoxLayout()

        title = QLabel("Operator Dashboard")
        title.setAlignment(Qt.AlignCenter)
        title.setStyleSheet("font-size: 20px; font-weight: bold;")
        layout.addWidget(title)

        # Buttons
        self.goods_receiving_btn = QPushButton("Goods Receiving")
        self.sales_btn = QPushButton("Sales")
        self.inventory_view_btn = QPushButton("Inventory View")

        layout.addWidget(self.goods_receiving_btn)
        layout.addWidget(self.sales_btn)
        layout.addWidget(self.inventory_view_btn)

        self.setLayout(layout)

        # Connect buttons to their respective functions
        self.goods_receiving_btn.clicked.connect(self.open_goods_receiving)
        self.sales_btn.clicked.connect(self.open_sales)
        self.inventory_view_btn.clicked.connect(self.view_inventory)

    def open_goods_receiving(self):
        self.goods_window = GoodsReceivingUI()
        self.goods_window.show()

    def open_sales(self):
        self.sales_window = SalesUI()
        self.sales_window.show()

    def view_inventory(self):
        self.inventory_window = InventoryViewUI()
        self.inventory_window.show()
