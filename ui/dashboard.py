from PySide6.QtWidgets import QMainWindow, QLabel

class DashboardWindow(QMainWindow):
    def __init__(self, username, role):
        super().__init__()
        self.setWindowTitle("Dashboard")
        self.setGeometry(100, 100, 600, 400)

        label = QLabel(f"Welcome {username}!\nRole: {role}", self)
        label.setGeometry(50, 50, 300, 50)
