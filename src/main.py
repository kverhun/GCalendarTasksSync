__author__ = 'Kostya'

import sys

from PyQt5.QtWidgets import QApplication, QWidget

from google_calendar_access import sync_google_data_with_database


class MainWidget(QWidget):

    def __init__(self):
        super().__init__()
        self.InitGUI()


    def InitGUI(self):
        self.resize(250, 150)
        self.move(300, 300)
        self.setWindowTitle('Application title')


if __name__ == '__main__':
    sync_google_data_with_database()

    app = QApplication(sys.argv)
    w = MainWidget()
    w.show()

    sys.exit(app.exec_())