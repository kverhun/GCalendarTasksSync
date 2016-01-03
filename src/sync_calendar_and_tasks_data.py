__author__ = 'Kostya'

from tasks_database_sync import get_tasks_list, task_exists, increment_task_time_spent, reset_all_tasks_time_spent
from connection import get_all_events


EVENT_NAME_PREFIX = '[id'
EVENT_NAME_SUFFIX = ']'



def sync_calendar_and_tasks_data():
    events = get_all_events()
    reset_all_tasks_time_spent()

    for event in events:
        event_name = event[1]
        print(event_name)
        if event_name.startswith(EVENT_NAME_PREFIX) and event_name.endswith(EVENT_NAME_SUFFIX):
            try:
                id = int(event_name[3:-1])
                print(id)
                if task_exists(id):
                    print("Task exists")
                    event_duration_seconds = event[3] - event[2]
                    print(event_duration_seconds)
                    increment_task_time_spent(id, event_duration_seconds)
                else:
                    print("Task does not exist")

            except ValueError:
                print('not valid id')