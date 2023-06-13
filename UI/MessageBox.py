from enum import Enum
from PyQt5.QtWidgets import QMessageBox


class AlertType(Enum):
    ERROR = [QMessageBox.Critical, "error"]
    WARNING = [QMessageBox.Warning, "warning"]
    INFO = [QMessageBox.Information, "Information"]


class AlertBox(QMessageBox):
    def __init__(self, alert_type: AlertType, content, parent=None):
        super().__init__(parent)
        icon, title = alert_type.value
        self.setWindowTitle(title.capitalize())
        self.setIcon(icon)
        self.setText(content)
        self.setStandardButtons(QMessageBox.Ok)
