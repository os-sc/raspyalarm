from datetime import datetime

from alarmconfig.repeaters.repeater import Repeater
from alarmconfig.data_types.date_string import DateString


class SingleDateRepeater(Repeater):
    def __init__(self):
        self._date = None
        super().__init__()

    def set_values(self, values):
        if not isinstance(values, DateString):
            raise TypeError('SingleDateRepeater only accepts a single DateString as value, got ' + str(type(values)))

    def is_active(self):
        return self._date.compare_with(datetime.now())
