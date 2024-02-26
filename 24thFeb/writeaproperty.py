"""
Write a simple Promo class. Its constructor receives two variables: name (which must be a string) and expires (which must be a datetime object).

Add a property called expired which returns a boolean value indicating whether the promo has expired or not.

Checkout the tests and datetime module for more info. Have fun!
"""

from datetime import datetime

NOW = datetime.now()


class Promo:
    def __init__(self, name, expires:datetime):
        self.name = name
        self.expires =expires

    # @property
    def expired(self):
        return self.expires <=NOW
        # if self.expires <= NOW:
        #     return True
        # else:
        #     return False

classobj = Promo('raj',datetime(year=2024, month=12, day=19))
print(classobj.expired())

