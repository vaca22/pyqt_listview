import json
import sys

import requests
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QDialog

from config import init_config
from custom_mainwindow import CustomMainwindow
from mainwindow import Ui_MainWindow
from paddleocr import PaddleOCR, draw_ocr
import cv2

if __name__ == '__main__':
    ocr = PaddleOCR(use_angle_cls=True, lang="en")
    img_path = "C:/Users/Administrator/Desktop/project/qt_wx/pyqt_listview/bb.png"
    img = cv2.imread(img_path)

    cap = cv2.VideoCapture(0)

    # read usb camera
    while True:
        # Capture frame-by-frame using opencv
        ret, frame = cap.read()
        if not ret:
            print("Error: failed to capture image")
            break
        img = frame
        result = ocr.ocr(img, cls=True)
        result_list = []
        if len(result) != 0:
            for idx in range(len(result)):
                res = result[idx]
                if res == None:
                    continue
                for idx2 in range(len(res)):
                    text = res[idx2][1][0]
                    result_list.append(text)

            print(result_list)
        cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # app = QApplication(sys.argv)
    # main_window = CustomMainwindow()
    # ui = Ui_MainWindow()
    # ui.setupUi(main_window)
    # main_window.closing.connect(ui.closeEvent)
    # main_window.show()
    # sys.exit(app.exec_())
