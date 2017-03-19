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
        self.UpdateFromGoogle()

    def InitGUI(self):
        self.ui = uic.loadUi('gui/MainWindow.ui', self)
        self.ui.syncButton.clicked.connect(self.UpdateFromGoogle)
        self.ui.addTaskButton.clicked.connect(self.OnTaskAdd)

    def OnTaskAdd(self):
        title = self.ui.taskTitleEdit.text()
        id = self.last_task_id + 1
        self.last_task_id = id

        parent_id_str = self.ui.parentIdEdit.text()

        if not parent_id_str:
            add_new_task(title, None)
        else:
            try:
                parent_id = int(parent_id_str)
                add_new_task(title, parent_id)
            except:
                add_new_task(title, None)
        self.UpdateTasksTable()
        self.ui.taskTitleEdit.clear()
        self.ui.parentIdEdit.clear()


    def UpdateTasksTable(self):
        self.ui.tasksTableWidget.setRowCount(0)
        tasks = get_tasks_list()
        for task in tasks:
            row_number = self.ui.tasksTableWidget.rowCount()
            self.ui.tasksTableWidget.insertRow(row_number)
            self.ui.tasksTableWidget.setItem(row_number, 0, QTableWidgetItem(str(task[0])))
            self.ui.tasksTableWidget.setItem(row_number, 1, QTableWidgetItem(task[1]))
            self.ui.tasksTableWidget.setItem(row_number, 2, QTableWidgetItem(str(task[2]/3600)))
            self.ui.tasksTableWidget.setItem(row_number, 3, QTableWidgetItem(str(task[3])))


    def UpdateFromGoogle(self):
        sync_google_data_with_database()
        sync_calendar_and_tasks_data()
        self.UpdateTasksTable()

