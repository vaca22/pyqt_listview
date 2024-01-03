import sys
from PyQt5.QtWidgets import QApplication,  QDialog


from TestDesigner import Ui_Dialog




if __name__ == '__main__':
    print('PyCharm')
    app = QApplication(sys.argv)
    Dialog = QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()

    sys.exit(app.exec_())
