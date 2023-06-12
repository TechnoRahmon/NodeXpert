from PyQt5.QtCore import Qt, QRect
from PyQt5.QtWidgets import QMainWindow, QTableWidget, QTableWidgetItem, QWidget, QPushButton, QVBoxLayout, \
    QInputDialog, QLineEdit, QStyledItemDelegate, QLabel

from .Table import NodeVersionsTable

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Node.js Versions")
        self.screen_high = 800
        self.screen_width = 600

        self.setGeometry(100, 100, self.screen_width, self.screen_high)
        # Create a central widget and set the layout
        central_layout = self.create_central_widget()

        self.add_title()

        self.table_widget = NodeVersionsTable(self)

        # Add a refresh button
        refresh_button = QPushButton("Refresh", self)
        refresh_button.clicked.connect(self.refreshNodeVersions)

        central_layout.addWidget(self.title_widget)
        central_layout.addWidget(self.table_widget)
        central_layout.addWidget(self.title_widget)
        central_layout.addWidget(refresh_button)

        # Set initial table data
        self.refreshNodeVersions()

    def create_central_widget(self):
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)
        central_layout = QVBoxLayout(central_widget)
        return central_layout

    def add_title(self):
        self.title_widget = QLabel("Node.js Versions", self)
        self.title_widget.setAlignment(Qt.AlignCenter)

    def refreshNodeVersions(self):
        node_versions = [
            {"version": "v14.17.0", "status": "active", "notes": "First version", "editable": True},
            {"version": "v12.22.6", "status": "inactive", "notes": "Old version", "editable": False},
            {"version": "v10.24.1", "status": "inactive", "notes": "Deprecated version", "editable": True}
        ]  # Replace with your logic to fetch the versions

        self.table_widget.setVersions(node_versions)

