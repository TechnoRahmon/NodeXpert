from PyQt5.QtWidgets import QWidget, QMainWindow, QVBoxLayout


class Widget(QWidget):
    def __init__(self, parent: QMainWindow=None, alignment=None):
        super().__init__(parent)
        parent.setCentralWidget(self)
        self.layout = QVBoxLayout(self)
        self.layout.setAlignment(alignment)
