class DateString():
    def __init__(self, value):
        self._string = '00000000'
        self.set_date(value)

    @property
    def day(self):
        return int(self._string[:2])

    @property
    def month(self):
        return int(self._string[2:4])

    @property
    def year(self):
        return int(self._string[4:])

    def set_date(self, v):
        if type(v) is int:
            v = str(v)
        if not isinstance(v, str):
            raise TypeError('Time must be either str or int, got ' + str(type(v)))

        v = DateString.left_pad(v)
        if not DateString.is_valid_date_string(v):
            raise ValueError('Value is not a valid time, got ' + str(v))
        else:
            self._string = v

    def __str__(self):
        return self._string

    def compare_with_datetime(self, dt):
        return True if str(self) == str(DateString.convert_from_datetime(dt)) else False

    def compare_with_string(self, string):
        return True if str(self) == string else False

    def compare_with(self, ds):
        return True if str(self) == str(ds) else False

    @staticmethod
    def convert_from_datetime(dt):
        day = str(dt.day) if dt.day > 9 else '0' + str(dt.day)
        month = str(dt.month) if dt.month > 9 else '0' + str(dt.month)
        return DateString(day + month + str(dt.year))

    @staticmethod
    def left_pad(string):
        missing = 8 - len(string)
        if missing > 0:
            string = missing * '0' + string
        return string

    @staticmethod
    def is_valid_date_string(string):
        if not type(string) is str:
            return False
        if not len(string) == 8:
            return False
        if not string.isdigit():
            return False
        if int(string[:2]) > 31:
            return False
        if int(string[2:4]) > 12:
            return False
        if int(string) < 0:
            return False
        return True
