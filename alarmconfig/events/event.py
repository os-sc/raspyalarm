from alarmconfig.data_types.time_string import TimeString

class Event():
    def __init__(self, name):
        if not name:
            raise ValueError('Name cannot be empty for Event')
        self.name = name
        self._time = None

    def setTime(self, time):
        self._time = TimeString(time)
