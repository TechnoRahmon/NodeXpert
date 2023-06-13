from PyQt5.QtWidgets import QPushButton
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt


# TODO ::
# 1. custom render button like 'refresh icon'
# 2. white panel to contain the button icon

class CustomButton(QPushButton):
    def __init__(self, text='', background_color=None, width=None, on_click=None, bold_text=False):
        super().__init__(text)
        self.set_custom_style(background_color, width, bold_text)
        if on_click:
            self.clicked.connect(on_click)

    def set_custom_style(self, background_color, width, bold_text):
        if background_color:
            self.setStyleSheet(f"background-color: {background_color};")

        if width:
            self.setFixedWidth(width)

        # Set default font
        font = QFont()
        font.setBold(bold_text)
        self.setFont(font)
