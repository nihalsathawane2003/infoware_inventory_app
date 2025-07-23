from PySide6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLabel, QListWidget

class UserManagementUI(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("User Management")
        self.setGeometry(100, 100, 400, 300)

        layout = QVBoxLayout()
        layout.addWidget(QLabel("User Roles: Admin, Operator, Supplier"))

        self.user_list = QListWidget()
        layout.addWidget(self.user_list)

        self.add_button = QPushButton("Add User")
        self.edit_button = QPushButton("Edit User")
        self.delete_button = QPushButton("Delete User")

        layout.addWidget(self.add_button)
        layout.addWidget(self.edit_button)
        layout.addWidget(self.delete_button)

        self.setLayout(layout)
