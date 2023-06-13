from enum import Enum
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout

from Controller.NvmController import NvmController
from .Label import CustomLabel
from UI.Table.Table import NodeVersionsTable
from .Button import CustomButton
from .Layout import Widget
from .MessageBox import AlertBox, AlertType

class ErrorMessages(Enum):
    VersionsEmpty = "There are no node js versions , check if the NVM is installed!"

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Node.js Versions")
        self.screen_high = 800
        self.screen_width = 600
        self.setWindowFlags(self.windowFlags() & ~Qt.WindowMaximizeButtonHint | Qt.MSWindowsFixedSizeDialogHint)
        self.setGeometry(100, 100, self.screen_width, self.screen_high)
        # set up a central widget and set the layout
        self.top_layout = Widget(self,Qt.AlignTop).layout

        # define the layout components
        self.setup_components()

        # adding the widgets
        self.top_layout.addWidget(self.main_title)
        self.top_layout.addWidget(self.table_widget)
        if len(self.table_widget.node_versions) == 0:
            self.top_layout.addWidget(self.error_message)
        self.top_layout.addStretch(1)
        self.top_layout.addWidget(self.refresh_button)



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
        self.error_message = CustomLabel(
            ErrorMessages.VersionsEmpty.value,
            font_size=10,
            font_color='red',
            font_weight=QFont.Bold,
            alignment=Qt.AlignLeft)

    def setup_table(self):
        # Set initial table data
        self.table_widget = NodeVersionsTable(self)
        self.refresh_node_versions()

    def refresh_node_versions(self):
        # get the nvm controller
        nvm_controller = NvmController()
        # get the node versions list
        node_versions = nvm_controller.get_node_versions_list()
        # set the list to the Table
        self.table_widget.set_versions(node_versions)


    def refresh_button_click(self):
        self.refresh_node_versions()
        if len(self.table_widget.node_versions) == 0:
           error_alert = AlertBox(AlertType.ERROR,ErrorMessages.VersionsEmpty.value)
           error_alert.exec_()

    def setup_buttons(self):
        self.refresh_button = CustomButton(
            "Refresh",
            width=200,
            on_click=self.refresh_button_click)
