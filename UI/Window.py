from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout

from .Label import CustomLabel
from UI.Table.Table import NodeVersionsTable
from .Button import CustomButton


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Node.js Versions")
        self.screen_high = 800
        self.screen_width = 600
        self.setWindowFlags(self.windowFlags() & ~Qt.WindowMaximizeButtonHint | Qt.MSWindowsFixedSizeDialogHint)
        self.setGeometry(100, 100, self.screen_width, self.screen_high)
        # set up a central widget and set the layout
        central_layout = self.setup_layout()

        # define the layout components
        self.setup_components()

        # adding the widgets
        central_layout.addWidget(self.main_title)
        central_layout.addWidget(self.table_widget)
        central_layout.addWidget(self.refresh_button)



    def setup_layout(self):
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)
        central_layout = QVBoxLayout(central_widget)
        central_layout.setAlignment(Qt.AlignTop)
        return central_layout

    def setup_components(self):
        self.setup_title()
        self.setup_table()
        self.setup_buttons()

    def setup_title(self):
        self.main_title = CustomLabel(
            "Node.js Versions",
            font_size=13,
            font_weight=QFont.Bold,
            alignment=Qt.AlignLeft)

    def setup_table(self):
        # Set initial table data
        self.table_widget = NodeVersionsTable(self)
        self.refresh_node_versions()

    def refresh_node_versions(self):
        node_versions = [
            {"version": "v14.17.0", "active": False, "notes": "First version", "editable": True},
            {"version": "v12.22.6", "active": True, "notes": "Old version", "editable": False},
            {"version": "v10.24.1", "active": False, "notes": "Deprecated version", "editable": True},
            {"version": "v10.24.1", "active": False, "notes": "ddddd", "editable": True}
        ]  # Replace with your logic to fetch the versions
        self.table_widget.set_versions(node_versions)


    def refresh_button_click(self):
        self.refresh_node_versions()

    def setup_buttons(self):
        self.refresh_button = CustomButton(
            "Click Me",
            width=200,
            on_click=self.refresh_button_click)
