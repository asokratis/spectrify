from __future__ import absolute_import, division, print_function, unicode_literals
from datetime import datetime

import ciso8601

epoch = datetime.utcfromtimestamp(0)


def timedelta_to_micros(td):
    return ((td.days * 86400 + td.seconds) * 1000) + (td.microseconds/1000)

def unix_time_nanos(dt):
    """Returns nanoseconds since epoch for a given datetime object"""
    return timedelta_to_micros(dt - epoch)

def iso8601_to_nanos(date_str):
    """ Returns a nanoseconds since epoch for a given ISO-8601 date string

        Arguments:
        date: ISO-8601 UTC datetime string (e.g. "2016-01-01 12:00:00.000000")

        Return Values:
        int representing # of nanoseconds since "1970-01-01" for date
    """
    dt = None
    counter = 0
    for test_value in (date_str, "1970-01-01"):
        try:
            dt = ciso8601.parse_datetime(test_value)
            break
        except Exception as e:
            print(str(e) + " - Defaulting " + str(date_str) + " to 1970-01-01")
            if counter == 0:
                counter += 1
                continue  # Ignore the exception and try the next type.
    return unix_time_nanos(dt)


def iso8601_to_days_since_epoch(date_str):
    dt = None
    counter = 0
    for test_value in (date_str, "1970-01-01"):
        try:
            dt = ciso8601.parse_datetime(test_value)
            break
        except Exception as e:
            print(str(e) + " - Defaulting " + str(date_str) + " to 1970-01-01")
            if counter == 0:
                counter += 1
                continue  # Ignore the exception and try the next type.
    return ((dt - epoch).days * 86400 * 1000)
