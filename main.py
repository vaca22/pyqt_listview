import json
import sys

import requests
from PyQt5.QtWidgets import QApplication,  QDialog


from TestDesigner import Ui_Dialog




if __name__ == '__main__':
    url = "http://vaca.vip:8569/authenticate"
    body = {
        "username": "13207759669",
        "password": "22345678"
    }
    response = requests.post(url, json=body, verify=False)
    json_data = json.loads(response.text)
    code = json_data["code"]
    if code == 0:
        app = QApplication(sys.argv)
        Dialog = QDialog()
        ui = Ui_Dialog()
        ui.setupUi(Dialog)
        Dialog.show()

        sys.exit(app.exec_())
