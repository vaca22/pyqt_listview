import sys
from PyQt5.QtWidgets import QApplication, QWidget, QListWidget, QListWidgetItem


class ListWidgetDemo(QListWidget):
    def __init__(self):
        super().__init__()
        self.resize(500, 500)
        self.setStyleSheet('font-size: 35px;')

        jan = 'Januaty'
        feb = 'g'
        mar = 'March'


        self.addItem(jan)
        self.addItem(QListWidgetItem(jan))
        self.addItem(feb)
        self.addItem(mar)


if __name__ == '__main__':
    print('PyCharm')
    app = QApplication(sys.argv)
    demo = ListWidgetDemo()
    demo.show()

    sys.exit(app.exec_())
