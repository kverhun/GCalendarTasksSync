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


def task_exists(task_id):
    connection = sqlite3.connect('../database/tasks.db')
    c = connection.cursor()
    c.execute('''select * from tasks where "id"=''' + str(task_id))
    res = c.fetchall()
    c.close()
    connection.commit()
    if len(res) == 1:
        return True
    else:
        return False


def reset_all_tasks_time_spent():
    connection = sqlite3.connect('../database/tasks.db')
    c = connection.cursor()
    c.execute('''update tasks set "spent_time"=(?)''', str(0))
    c.close()
    connection.commit()


def increment_task_time_spent(task_id, duration_seconds):
    print('increment_task_time_spent')
    connection = sqlite3.connect('../database/tasks.db')
    c = connection.cursor()
    print('cursor created')
    c.execute('''select * from tasks where "id"='''+str(task_id))
    current_duration = c.fetchone()[2]
    print(current_duration)
    c.execute(
        '''update tasks
           set "spent_time" = (?)
           where "id"=(?)''',
        (current_duration + duration_seconds, task_id))
    print('increment spent time, id:', id, 'time:', current_duration + duration_seconds)
    c.close()
    connection.commit()