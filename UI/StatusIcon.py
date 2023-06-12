from PyQt5.QtWidgets import QStyledItemDelegate
from PyQt5.QtCore import Qt, QRect


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
