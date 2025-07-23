from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QListWidget

class InventoryViewUI(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Inventory View")
        self.setGeometry(100, 100, 400, 400)

        layout = QVBoxLayout()

        layout.addWidget(QLabel("Current Inventory Levels"))
        self.inventory_list = QListWidget()
        layout.addWidget(self.inventory_list)

        self.setLayout(layout)
