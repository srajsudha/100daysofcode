"""
Write a generator that returns every 100th day counting forward from the PYBITES_BORN date.

Here is how the generator would work if you import and use it in your REPL:

>>> from itertools import islice
>>> from pprint import pprint as pp
>>> from gendates import gen_special_pybites_dates
>>> gen = gen_special_pybites_dates()
>>> pp(list(islice(gen, 5)))
[datetime.datetime(2017, 3, 29, 0, 0),
 datetime.datetime(2017, 7, 7, 0, 0),
 datetime.datetime(2017, 10, 15, 0, 0),
 datetime.datetime(2018, 1, 23, 0, 0),
 datetime.datetime(2018, 5, 3, 0, 0)]
"""

from datetime import datetime, timedelta
from itertools import islice
from pprint import pprint as pp

PYBITES_BORN = datetime(year=2016, month=12, day=19)

# hundreddays= PYBITES_BORN + timedelta(days=100)
# print(hundreddays)


def gen_special_pybites_dates():
    current_date = PYBITES_BORN
    days_of_increment = 100
    while True:
        current_date  = current_date + timedelta(days=days_of_increment)
        yield current_date


test = gen_special_pybites_dates()
pp(list(islice(test, 10)))
# pp(list(test))