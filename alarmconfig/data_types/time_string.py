class TimeString():
    def __init__(self, value):
        self._string = '0000'
        self.set_time(value)

    @property
    def hours(self):
        return int(self._string[:2])

    @property
    def minutes(self):
        return int(self._string[2:])

    def set_time(self, v):
        if type(v) is int:
            v = str(v)
        if not isinstance(v, str):
            raise TypeError('Time must be either str or int, got ' + str(type(v)))

        v = TimeString.left_pad(v)
        if not TimeString.is_valid_time_string(v):
            raise ValueError('Value is not a valid time, got ' + str(v))
        else:
            self._string = v

    def __str__(self):
        return self._string

    def compare_with_datetime(self, dt):
        return True if str(self) == str(TimeString.convert_from_datetime(dt)) else False

    def compare_with_string(self, string):
        return True if str(self) == string else False

    def compare_with(self, ds):
        return True if str(self) == str(ds) else False

    @staticmethod
    def convert_from_datetime(dt):
        hour = str(dt.hour) if dt.hour > 9 else '0' + str(dt.hour)
        minute = str(dt.minute) if dt.minute > 9 else '0' + str(dt.minute)
        return TimeString(hour + minute)

    @staticmethod
    def left_pad(string):
        missing = 4 - len(string)
        if missing > 0:
            string = missing * '0' + string
        return string

    @staticmethod
    def is_valid_time_string(string):
        if not type(string) is str:
            return False
        if not len(string) == 4:
            return False
        if not string.isdigit():
            return False
        if int(string[:2]) > 23:
            return False
        if int(string[2:]) > 59:
            return False
        if int(string) < 0:
            return False
        return True
