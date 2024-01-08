from io import BytesIO

import requests
from PyQt5 import QtGui, QtCore
from PyQt5.QtWidgets import QLabel, QVBoxLayout, QWidget, QApplication, QDialog
import qrcode


class QRCodeWindow(QDialog):
    def __init__(self, qr, text, parent=None):
        super(QRCodeWindow, self).__init__(parent)
        self.setWindowTitle("充值信息")
        self.layout = QVBoxLayout()
        self.resize(400, 400)

        self.img_lb = QLabel(self)
        self.img_lb.setAlignment(QtCore.Qt.AlignCenter)
        self.setLayout(self.layout)


        if qr is not None:
            if len(qr) != 0:
                url_img = qr
                pixmap = QtGui.QPixmap()
                pixmap.loadFromData(requests.get(url_img).content)
                # resize
                pixmap = pixmap.scaled(200, 200, QtCore.Qt.KeepAspectRatio)
                self.img_lb.setPixmap(pixmap)
                self.layout.addWidget(self.img_lb)
        self.contect_lb = QLabel(self)
        self.contect_lb.setText(text)
        self.layout.addWidget(self.contect_lb)
        self.setWindowFlag(QtCore.Qt.WindowContextHelpButtonHint, False)
