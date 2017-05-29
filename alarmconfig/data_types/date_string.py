class DateString():
    def __init__(self, value):
        self._string = '00000000'
        self.set_date(value)

    def set_date(self, v):
        if type(v) is int:
            v = str(v)
        if not type(v) is str:
            raise TypeError('Time must be either str or int, got ' + str(type(v)))

        v = DateString.left_pad(v)
        if not DateString.is_valid_date_string(v):
            raise ValueError('Value is not a valid time, got ' + str(v))
        else:
            self._string = v

    def __str__(self):
        return self._string

    @property
    def day(self):
        return int(self._string[:2])

    @property
    def month(self):
        return int(self._string[2:4])

    @property
    def year(self):
        return int(self._string[4:])

    def compare_with(self, other):
        pass

    @staticmethod
    def convert_from_datetime(dt):
        return DateString(str(dt.day) + str(dt.month) + str(dt.year))

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
