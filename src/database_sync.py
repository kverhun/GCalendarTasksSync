__author__ = 'Kostya'

from utils import rfc3339_to_unix_time

from connection import insert_task, clear_events_table

def sync_database_with_retrieved_data(event_items):
    clear_events_table()
    for event in event_items:
        insert_task(
            event['id'],
            event['summary'],
            rfc3339_to_unix_time(event['start'].get('dateTime')),
            rfc3339_to_unix_time(event['end'].get('dateTime'))
        )