import sys

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QListWidget, QListWidgetItem, QMainWindow

from untitled import Ui_MainWindow


class ListWidgetDemo(QListWidget):
    def __init__(self):
        super().__init__()
        self.resize(500, 500)
        self.setStyleSheet('font-size: 35px;')

        jan = 'Januaty'
        feb = 'g'
        mar = 'March'

        self.addItem(jan)
        # self.addItem(QListWidgetItem(jan))
        self.addItem(feb)
        self.addItem(mar)

        self.addItems([jan, feb])

        self.itemDoubleClicked.connect(self.getItem)

    def getItem(self, lstItem):
        print(self.currentItem().text())
        print(lstItem.text())
        print(self.currentRow())


class MyWindows(QMainWindow,Ui_MainWindow):
    def __init__(self):
        super(MyWindows, self).__init__()
        self.setGeometry(200, 200, 300, 300)
        self.setWindowTitle("gaga")
        self.initUI()
        self.setupUi(self)

    def initUI(self):
        self.label = QtWidgets.QLabel(self)
        self.label.setText("gaga")
        self.label.move(20, 50)

        self.b1 = QtWidgets.QPushButton(self)
        self.b1.setText("Click me")
        self.b1.clicked.connect(self.clicked)

    def clicked(self):
        self.label.setText("you press the button")
        self.update()

    def update(self):
        self.label.adjustSize()


if __name__ == '__main__':
    print('PyCharm')
    app = QApplication(sys.argv)
    demo = MyWindows()
    demo.show()

    sys.exit(app.exec_())
