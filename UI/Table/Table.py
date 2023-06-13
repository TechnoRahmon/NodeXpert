import sys
from PyQt5.QtWidgets import QTableWidget, QAbstractItemView, QHeaderView, QSizePolicy
from PyQt5.QtCore import Qt
from UI.StatusDelegate import StatusDelegate
from UI.Table.TableItem import TableItem


class NodeVersionsTable(QTableWidget):
    def __init__(self, parent=None):
        self.Headers_Labels = ["Version", "Status", "Notes"]
        # to define which column is editable
        self.Editable_columns = ["Notes"]

        super().__init__(parent)
        self.setSelectionMode(QAbstractItemView.NoSelection)

        self.setColumnCount(3)

        self.setHorizontalHeaderLabels(self.Headers_Labels)
        self.setColumnWidth(0, 100)
        self.setColumnWidth(1, 75)
        self.setColumnWidth(2, 375)

        # Set the stretch behavior of the columns
        self.horizontalHeader().setSectionResizeMode(0, QHeaderView.Fixed)
        self.horizontalHeader().setSectionResizeMode(1, QHeaderView.Fixed)
        self.horizontalHeader().setSectionResizeMode(2, QHeaderView.Stretch)

        # Set the vertical size policy of the table widget
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)

        # click event handler
        self.cellClicked.connect(self._status_click_handler)

    def set_versions(self, node_versions):
        self.clearContents()
        self.setRowCount(len(node_versions))
        self.node_versions = node_versions

        for row, info in enumerate(node_versions):
            for index, headerLabel in enumerate(self.Headers_Labels):
                editable = True if headerLabel in self.Editable_columns else False
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
        self.setMinimumHeight(300)

    # TODO :
    # 1. Notes on change handler (save on enter key)
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
