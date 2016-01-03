__author__ = 'Kostya'

import sys

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5 import uic

from google_calendar_access import sync_google_data_with_database


class MainWidget(QWidget):

    def __init__(self):
        super().__init__()
        self.ui = None
        self.InitGUI()

    def InitGUI(self):
        self.ui = uic.loadUi('gui/MainWindow.ui', self)
        self.ui.syncButton.clicked.connect(sync_google_data_with_database)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MainWidget()
    w.show()
    sys.exit(app.exec_())