from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QMainWindow


class CustomMainwindow(QMainWindow):
    def __init__(self):
        super().__init__()
    closing = pyqtSignal()

    def closeEvent(self, event):
        self.closing.emit()
        super().closeEvent(event)
