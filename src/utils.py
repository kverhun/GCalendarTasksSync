__author__ = 'Kostya'

import datetime
import time

def rfc3339_to_unix_time(rfc3339_time_str):
    # skip time zone for now
    str_to_convert = rfc3339_time_str[:-6]
    list = datetime.datetime.strptime(str_to_convert, '%Y-%m-%dT%H:%M:%S')
    return time.mktime(list.timetuple())
