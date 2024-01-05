import json
import sys

import requests
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication,  QDialog

from mainwindow import Ui_MainWindow


if __name__ == '__main__':
    app = QApplication(sys.argv)
    # class Ui_MainWindow(object):
    #     def setupUi(self, MainWindow):

    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()



    sys.exit(app.exec_())
