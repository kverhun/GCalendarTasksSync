__author__ = 'Kostya'

from PyQt5 import uic
from PyQt5.QtWidgets import QWidget

from google_calendar_access import sync_google_data_with_database

class MainWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.ui = None
        self.InitGUI()

    def InitGUI(self):
        self.ui = uic.loadUi('gui/MainWindow.ui', self)
        self.ui.syncButton.clicked.connect(sync_google_data_with_database)