import sys
from PyQt5.QtWidgets import QApplication
from UI.Window import MainWindow

def _start_app():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    _start_app()

# TODO:
# NVM version buttons : if NVM not installed > disable the table list
# Stop all node instance

# v2
# install node version
# crud start/stop your npm project
# log error expand > show terminal section
