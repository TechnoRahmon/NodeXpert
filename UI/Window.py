from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QMainWindow, QWidget, QPushButton, QVBoxLayout, QLabel

from .Label import CustomLabel
from .Table import NodeVersionsTable


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Node.js Versions")
        self.screen_high = 800
        self.screen_width = 600
        self.setWindowFlags(self.windowFlags() & ~Qt.WindowMaximizeButtonHint | Qt.MSWindowsFixedSizeDialogHint)
        self.setGeometry(100, 100, self.screen_width, self.screen_high)
        # Create a central widget and set the layout
        central_layout = self.create_central_widget()

        self.add_title()

        self.table_widget = NodeVersionsTable(self)

        # Add a refresh button
        refresh_button = QPushButton("Refresh", self)
        refresh_button.clicked.connect(self.refreshNodeVersions)

        central_layout.addWidget(self.MainTitle)
        central_layout.addWidget(self.table_widget)
        central_layout.addWidget(refresh_button)

        # Set initial table data
        self.refreshNodeVersions()

    def create_central_widget(self):
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)
        central_layout = QVBoxLayout(central_widget)
        central_layout.setAlignment(Qt.AlignTop)
        return central_layout

    def add_title(self):
        self.MainTitle = CustomLabel(
                            "Node.js Versions",
                            font_size=13,
                            font_weight=QFont.Bold,
                            alignment=Qt.AlignLeft)

    def refreshNodeVersions(self):
        node_versions = [
            {"version": "v14.17.0", "status": "active", "notes": "First version", "editable": True},
            {"version": "v12.22.6", "status": "inactive", "notes": "Old version", "editable": False},
            {"version": "v10.24.1", "status": "inactive", "notes": "Deprecated version", "editable": True},
            {"version": "v10.24.1", "status": "inactive", "notes": "ddddd", "editable": True}
        ]  # Replace with your logic to fetch the versions

        self.table_widget.setVersions(node_versions)
