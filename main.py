# main.py

from PySide6.QtWidgets import QApplication, QWidget, QStackedLayout
from ui.login_ui import LoginWindow
from ui.admin_dashboard import AdminDashboard
from ui.operator_dashboard import OperatorDashboard
import sys

class MainApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Inventory Management System")
        self.setGeometry(100, 100, 1000, 700)

        # Layout to switch between login and dashboards
        self.layout = QStackedLayout()
        self.setLayout(self.layout)

        # Initialize Login Window
        self.login_window = LoginWindow()
        self.login_window.login_success.connect(self.load_dashboard)  # Custom signal
        self.layout.addWidget(self.login_window)

    def load_dashboard(self, role):
        """Load the dashboard based on user role"""
        if role.lower() == "admin":
            self.dashboard = AdminDashboard()
        elif role.lower() == "operator":
            self.dashboard = OperatorDashboard()
        else:
            print(f"Unknown role: {role}")
            return

        self.layout.addWidget(self.dashboard)
        self.layout.setCurrentWidget(self.dashboard)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    sys.exit(app.exec())
