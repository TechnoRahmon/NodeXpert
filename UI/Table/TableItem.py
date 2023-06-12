from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QTableWidgetItem


class TableItem:
    def __init__(self, info, editable=False):
        self.item = QTableWidgetItem(info)

        if not editable:
            self.item.setFlags(self.item.flags() & ~Qt.ItemIsEditable)