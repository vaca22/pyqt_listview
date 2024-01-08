from io import BytesIO
from PyQt5 import QtGui, QtCore
from PyQt5.QtWidgets import QLabel, QVBoxLayout, QWidget, QApplication, QDialog
import qrcode



class QRCodeWindow(QDialog):
    def __init__(self, qr,text, parent=None):
        super(QRCodeWindow,self).__init__(parent)
        self.setWindowTitle("充值信息")
        self.layout = QVBoxLayout()

        self.contect_lb = QLabel(self)
        self.contect_lb.setText(text)
        # self.contect_lb.setAlignment(QtCore.Qt.AlignTop)
        self.layout.addWidget(self.contect_lb)
        self.img_lb = QLabel(self)
        self.img_lb.setAlignment(QtCore.Qt.AlignCenter)
        self.setLayout(self.layout)
        self.resize(400, 400)



        if qr is not None:
            if len(qr) != 0:
                buffer = BytesIO()
                qr_img = qrcode.make(qr)
                qr_img.save(buffer, format='png')
                pixmap = QtGui.QPixmap()
                pixmap.loadFromData(buffer.getvalue())
                self.img_lb.setPixmap(pixmap)
                self.layout.addWidget(self.img_lb)
        self.setWindowFlag(QtCore.Qt.WindowContextHelpButtonHint, False)



