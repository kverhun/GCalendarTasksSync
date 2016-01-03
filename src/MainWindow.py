__author__ = 'Kostya'

from PyQt5 import uic
from PyQt5.QtWidgets import QWidget, QTableWidgetItem

from google_calendar_access import sync_google_data_with_database
from tasks_database_sync import add_new_task, get_tasks_list
from sync_calendar_and_tasks_data import sync_calendar_and_tasks_data

class MainWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.ui = None
        self.last_task_id = 0
        self.InitGUI()

    def InitGUI(self):
        self.ui = uic.loadUi('gui/MainWindow.ui', self)
        self.ui.syncButton.clicked.connect(self.UpdateFromGoogle)
        self.ui.addTaskButton.clicked.connect(self.OnTaskAdd)
        self.UpdateTasksTable()

    def OnTaskAdd(self):
        title = self.ui.taskTitleEdit.text()
        id = self.last_task_id + 1
        self.last_task_id = id
        print('New task: title', title, 'id:', id)
        add_new_task(title)
        self.UpdateTasksTable()

    def UpdateTasksTable(self):
        self.ui.tasksTableWidget.setRowCount(0)
        tasks = get_tasks_list()
        for task in tasks:
            row_number = self.ui.tasksTableWidget.rowCount()
            self.ui.tasksTableWidget.insertRow(row_number)
            self.ui.tasksTableWidget.setItem(row_number, 0, QTableWidgetItem(str(task[0])))
            self.ui.tasksTableWidget.setItem(row_number, 1, QTableWidgetItem(task[1]))
            self.ui.tasksTableWidget.setItem(row_number, 2, QTableWidgetItem(str(task[2]/3600)))

    def UpdateFromGoogle(self):
        sync_google_data_with_database()
        sync_calendar_and_tasks_data()
        self.UpdateTasksTable()

