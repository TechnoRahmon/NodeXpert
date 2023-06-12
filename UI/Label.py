from PyQt5.QtWidgets import QLabel
from PyQt5.QtGui import QFont, QColor
from PyQt5.QtCore import Qt


class CustomLabel(QLabel):
    def __init__(
            self, text='',
            font_size=12,
            font_color='black',
            font_weight=QFont.Normal,
            alignment=Qt.AlignLeft):
        super().__init__(text)
        self.setCustomFont(font_size, font_color, font_weight)
        self.setAlignment(alignment)
        self.setFixedHeight(font_size+15)
    def setCustomFont(self, font_size, font_color, font_weight):
        font = QFont()
        font.setPointSize(font_size)
        font.setWeight(font_weight)
        self.setFont(font)
        self.setStyleSheet(f"color: {font_color};")