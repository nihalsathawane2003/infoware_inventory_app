# ui/login_ui.py

from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QComboBox
from PySide6.QtCore import Signal
from models.user_model import verify_user

class LoginWindow(QWidget):
    login_success = Signal(str)  # Emits the role string

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Login")

        layout = QVBoxLayout()
        self.username_input = QLineEdit()
        self.username_input.setPlaceholderText("Username")

        self.password_input = QLineEdit()
        self.password_input.setPlaceholderText("Password")
        self.password_input.setEchoMode(QLineEdit.Password)

        self.role_dropdown = QComboBox()
        self.role_dropdown.addItems(["Admin", "Operator"])

        self.login_button = QPushButton("Login")
        self.login_button.clicked.connect(self.handle_login)

        self.message_label = QLabel()

        layout.addWidget(QLabel("Username"))
        layout.addWidget(self.username_input)
        layout.addWidget(QLabel("Password"))
        layout.addWidget(self.password_input)
        layout.addWidget(QLabel("Select Role"))
        layout.addWidget(self.role_dropdown)
        layout.addWidget(self.login_button)
        layout.addWidget(self.message_label)

        self.setLayout(layout)

    def handle_login(self):
        username = self.username_input.text()
        password = self.password_input.text()
        role = self.role_dropdown.currentText()

        user = verify_user(username, password, role)
        if user:
            self.login_success.emit(role)  # Send signal to main
        else:
            self.message_label.setText("Invalid username or password")
