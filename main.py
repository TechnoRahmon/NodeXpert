# This is a sample Python script.
import sys
from PyQt5.QtWidgets import QApplication


from UI.Window import MainWindow

def _start_app():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    _start_app()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
