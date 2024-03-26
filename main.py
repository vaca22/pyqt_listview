import json
import sys

import requests
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication,  QDialog

from config import init_config
from custom_mainwindow import CustomMainwindow
from mainwindow import Ui_MainWindow
from paddleocr import PaddleOCR, draw_ocr
import cv2





if __name__ == '__main__':
    ocr = PaddleOCR(use_angle_cls=True, lang="en")
    img_path = "C:/Users/Administrator/Desktop/project/qt_wx/pyqt_listview/bb.png"
    img=cv2.imread(img_path)


    result = ocr.ocr(img, cls=True)
    result_list = []
    for idx in range(len(result)):
        res = result[idx]
        for idx2 in range(len(res)):
            text = res[idx2][1][0]
            result_list.append(text)

    print(result_list)
    # app = QApplication(sys.argv)
    # main_window = CustomMainwindow()
    # ui = Ui_MainWindow()
    # ui.setupUi(main_window)
    # main_window.closing.connect(ui.closeEvent)
    # main_window.show()
    # sys.exit(app.exec_())
