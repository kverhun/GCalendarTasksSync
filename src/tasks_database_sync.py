__author__ = 'Kostya'

import sqlite3

def add_new_task(title):
    connection = sqlite3.connect('../database/tasks.db')
    c = connection.cursor()
    c.execute('''insert into tasks (title, spent_time) values (?,?)''', [title, 0])
    c.close()
    connection.commit()


def get_tasks_list():
    connection = sqlite3.connect('../database/tasks.db')
    c = connection.cursor()
    c.execute('''select * from tasks''')
    res = c.fetchall()
    c.close()
    connection.commit()
    return res