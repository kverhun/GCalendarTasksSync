__author__ = 'Kostya'

from PyQt5 import uic
from PyQt5.QtWidgets import QWidget, QTableWidgetItem

from google_calendar_access import sync_google_data_with_database

class MainWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.ui = None
        self.last_task_id = 0
        self.InitGUI()

    def InitGUI(self):
        self.ui = uic.loadUi('gui/MainWindow.ui', self)
        self.ui.syncButton.clicked.connect(sync_google_data_with_database)
        self.ui.addTaskButton.clicked.connect(self.OnTaskAdd)

    def OnTaskAdd(self):
        title = self.ui.taskTitleEdit.text()
        id = self.last_task_id + 1
        self.last_task_id = id
        print('New task: title', title, 'id:', id)
        row_number = self.ui.tasksTableWidget.rowCount()
        self.ui.tasksTableWidget.insertRow(row_number)
        self.ui.tasksTableWidget.setItem(row_number, 0, QTableWidgetItem(str(id)))
        self.ui.tasksTableWidget.setItem(row_number, 1, QTableWidgetItem(title))
        self.ui.tasksTableWidget.setItem(row_number, 2, QTableWidgetItem(str(0)))
