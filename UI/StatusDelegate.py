
from PyQt5.QtCore import Qt, QRect
from PyQt5.QtWidgets import QStyledItemDelegate


class StatusDelegate(QStyledItemDelegate):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.table = parent

    def paint(self, painter, option, index):
        # get the cell coordinates
        row = index.row()
        col = index.column()
        # get the info obj
        info_obj = self.table.node_versions[row]

        # check if the cell is active then give green background : else red background
        if info_obj['active'] and col == 1:
            painter.setBrush(Qt.green)
        else :
            painter.setBrush(Qt.red)

        # render the circle
        radius = 10

        rect = QRect(option.rect.x() + (option.rect.width() - radius) // 2,
                     option.rect.y() + (option.rect.height() - radius) // 2,
                     radius,
                     radius)
        painter.drawEllipse(rect)
        super().paint(painter, option, index)