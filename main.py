import json
import sys

import requests
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication,  QDialog

from config import init_config
from custom_mainwindow import CustomMainwindow
from mainwindow import Ui_MainWindow


def auth():
    url = "http://1.14.135.210:8569/authenticate"
    body = {
        "username": "15769415445",
        "password": "22345678"
    }
    response = requests.post(url, json=body, verify=False)
    json_data = json.loads(response.text)
    code = json_data["code"]
    return code == 0




if __name__ == '__main__':
    init_config()
    if auth() is False:
        print("认证失败")
        sys.exit(0)
    app = QApplication(sys.argv)
    main_window = CustomMainwindow()
    ui = Ui_MainWindow()
    ui.setupUi(main_window)
    main_window.closing.connect(ui.closeEvent)
    main_window.show()
    sys.exit(app.exec_())
