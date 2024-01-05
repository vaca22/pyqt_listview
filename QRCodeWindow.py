from io import BytesIO
from PyQt5 import QtGui, QtCore
from PyQt5.QtWidgets import QLabel, QVBoxLayout, QWidget, QApplication, QDialog
import qrcode



class QRCodeWindow(QDialog):
    def __init__(self, text,parent=None):
        super(QRCodeWindow,self).__init__(parent)
        self.setWindowTitle("QR Code")
        self.layout = QVBoxLayout()
        self.label = QLabel(self)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.layout.addWidget(self.label)
        self.setLayout(self.layout)
        self.resize(400, 400)
        buffer = BytesIO()
        qr_img = qrcode.make(text)
        qr_img.save(buffer, format='png')
        pixmap = QtGui.QPixmap()
        pixmap.loadFromData(buffer.getvalue())
        self.label.setPixmap(pixmap)
        self.setWindowFlag(QtCore.Qt.WindowContextHelpButtonHint, False)



