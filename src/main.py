__author__ = 'Kostya'

import sys

from PyQt5.QtWidgets import QApplication, QWidget

from google_calendar_access import sync_google_data_with_database


if __name__ == '__main__':
    sync_google_data_with_database()

    app = QApplication(sys.argv)
    w = QWidget()
    w.resize(250, 150)
    w.move(300, 300)
    w.setWindowTitle('Application title')
    w.show()

    sys.exit(app.exec_())