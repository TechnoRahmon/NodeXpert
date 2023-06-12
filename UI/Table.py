import sys
from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem, QStyledItemDelegate, QAbstractItemView
from PyQt5.QtCore import Qt, QRect



class TableItem:
    def __init__(self, info, editable=False):
        self.item = QTableWidgetItem(info)
        if not editable:
            self.item.setFlags(self.item.flags() & ~Qt.ItemIsEditable)

class NodeVersionsTable(QTableWidget):
    def __init__(self, parent=None):
        self.Headers_Labels = ["Version", "Status", "Notes"]
        super().__init__(parent)
        self.setFixedWidth(600)
        self.setMaximumHeight(300)
        self.setSelectionMode(QAbstractItemView.NoSelection)

        self.setColumnCount(3)
        self.setHorizontalHeaderLabels(self.Headers_Labels)
        self.setColumnWidth(0, 100)
        self.setColumnWidth(1, 100)
        self.setColumnWidth(2, 375)

    def setVersions(self, node_versions):
        self.clearContents()
        self.setRowCount(len(node_versions))
        # self.setEditTriggers(QTableWidget.EditTrigger.NoEditTriggers)
        columns = self.columnCount()

        for row, info in enumerate(node_versions):
            for index, headerLabel in enumerate(self.Headers_Labels):
                editable = True if headerLabel == self.Headers_Labels[2] else False
                tableItem = TableItem(info[headerLabel.lower()], editable)
                self.setItem(row, index, tableItem.item)


    def update_notes(self, row):
        notes_item = self.table_widget.item(row, 2)
        # new_notes, ok = QInputDialog.getText(self, "Update Notes", "Enter new notes:", QLineEdit.Normal,
        #                                      notes_item.text())
        # if ok:
        #     notes_item.setText(new_notes)


class StatusDelegate(QStyledItemDelegate):
    def paint(self, painter, option, index):
        status = index.data(Qt.DisplayRole)
        if status == "active":
            painter.setBrush(Qt.green)
        else:
            painter.setBrush(Qt.red)

        radius = 8
        rect = QRect(option.rect.x() + (option.rect.width() - radius) // 2,
                     option.rect.y() + (option.rect.height() - radius) // 2, radius, radius)
        painter.drawEllipse(rect)

        super().paint(painter, option, index)
