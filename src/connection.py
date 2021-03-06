__author__ = 'Kostya'

import sqlite3


def create_database():
    connection = sqlite3.connect('../database/tasks.db')
    c = connection.cursor()
    c.execute('''create table if not exists calendar_items (id text primary key, title text, time_start integer, time_end integer)''')
    c.execute('''create table if not exists tasks (id integer primary key, title text, spent_time integer)''')
    connection.commit()


def insert_task(id, title, time_start, time_end):
    connection = sqlite3.connect('../database/tasks.db')
    c = connection.cursor()
    print(title)
    c.execute('''insert into calendar_items values (?,?,?,?)''',
              [id, title, time_start, time_end])
    c.close()
    connection.commit()


def clear_events_table():
    connection = sqlite3.connect('../database/tasks.db')
    c = connection.cursor()
    c.execute('''delete from calendar_items''')
    c.close()
    connection.commit()


def get_all_events():
    connection = sqlite3.connect('../database/tasks.db')
    c = connection.cursor()
    c.execute('''select * from calendar_items''')
    res = c.fetchall()
    c.close()
    return res

