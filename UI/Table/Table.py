import sys
from PyQt5.QtWidgets import QTableWidget, QAbstractItemView, QHeaderView, QSizePolicy
from PyQt5.QtCore import Qt
from Model.NodeVersion import NoteItem
from UI.MessageBox import AlertType
from UI.StatusDelegate import StatusDelegate
from UI.Table.TableItem import TableItem


class NodeVersionsTable(QTableWidget):
    def __init__(self, parent=None):
        self.Headers_Labels = ["Version", "Status", "Notes"]
        # to define which column is editable
        self.Editable_columns = ["Notes"]

        super().__init__(parent)
        self.setSelectionMode(QAbstractItemView.NoSelection)
        self.window_widget = parent
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

        # change event handler
        self.cellChanged.connect(self._update_notes_handler)

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
    def _update_notes_handler(self, row, column):
        NOTE_COLUMN = self.Headers_Labels.index('Notes')
        VERSION_COLUMN = self.Headers_Labels.index('Version')
        if column == NOTE_COLUMN:
            old_note = self.node_versions[row]['notes']
            new_note = self.item(row, column).text()
            # check if the update is a new update
            if old_note != new_note:
                version = self.item(row, VERSION_COLUMN).text()
                note_item = NoteItem(new_note, version)
                self.window_widget.nvm_controller.update_notes(note_item)


    def _status_click_handler(self, row, column):
        if (column == 1):
            # inactive all the versions in the table UI
            new_dict = list(map(lambda row: {**row, 'active': False}, self.node_versions))
            # set the active cell
            new_dict[row]['active'] = True
            # get the version number
            version_no = new_dict[row]['version']
            # execute the nvm use command
            status, message = self.window_widget.nvm_controller.set_new_active_version(version_no)
            # if the execution is not succeeded, then alert with error message
            if not status:
                return self.window_widget.show_alert_message(message, AlertType.ERROR)
            # update the table
            self.set_versions(new_dict)
            self.window_widget.show_alert_message(message)

