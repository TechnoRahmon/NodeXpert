import sys
from PyQt5.QtWidgets import QTableWidget, QAbstractItemView, QHeaderView
from PyQt5.QtCore import Qt
from UI.StatusDelegate import StatusDelegate
from UI.Table.TableItem import TableItem


class NodeVersionsTable(QTableWidget):
    def __init__(self, parent=None):
        self.Headers_Labels = ["Version", "Status", "Notes"]
        # to define which column is
        self.exclude_fields = ["active"]

        super().__init__(parent)
        self.setSelectionMode(QAbstractItemView.NoSelection)

        self.setColumnCount(3)

        self.setHorizontalHeaderLabels(self.Headers_Labels)
        self.setColumnWidth(0, 100)
        self.setColumnWidth(1, 75)
        self.setColumnWidth(2, 375)
        # set the fixed width of the table to be 100% of the container
        self.horizontalHeader().setSectionResizeMode(2, QHeaderView.Stretch)

        # click event handler
        self.cellClicked.connect(self._status_click_handler)

    def set_versions(self, node_versions):
        self.clearContents()
        self.setRowCount(len(node_versions))
        self.node_versions = node_versions

        for row, info in enumerate(node_versions):
            for index, headerLabel in enumerate(self.Headers_Labels):
                editable = True if headerLabel in self.exclude_fields else False
                content = '' if headerLabel == self.Headers_Labels[1] else info[headerLabel.lower()]
                tableItem = TableItem(content, editable)
                tableItem.item.setTextAlignment(Qt.AlignCenter)
                self.setItem(row, index, tableItem.item)

        self.render_status()

        self.resizeRowToContents(len(node_versions))

        self.set_high(len(node_versions))

    def render_status(self):
        # Set the delegate for the status column
        status_delegate = StatusDelegate(self)
        self.setItemDelegateForColumn(1, status_delegate)

    def set_high(self, node_count):
        # set the table high from the length of the rows
        self.setFixedHeight(45 * node_count + 8)
        self.setMinimumHeight(200)

    def update_notes(self, row):
        notes_item = self.table_widget.item(row, 2)
        # new_notes, ok = QInputDialog.getText(self, "Update Notes", "Enter new notes:", QLineEdit.Normal,
        #                                      notes_item.text())
        # if ok:
        #     notes_item.setText(new_notes)

    def _status_click_handler(self, row, column):
        if (column == 1):
            # set new dict > all columns to inactive
            status_column_index = 1  # Assuming the status column index is 1
            new_dict = list(map(lambda row: {**row, 'active': False}, self.node_versions))
            # set the active cell
            new_dict[row]['active'] = True
            # update the table
            self.set_versions(new_dict)
