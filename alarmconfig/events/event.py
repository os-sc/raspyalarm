from alarmconfig.data_types.time_string import TimeString

class Event():
    def __init__(self, name):
        if not name:
            raise ValueError('Name cannot be empty for Event')
        self.name = name
        self._actions = []
        self._time = None

    def execute_actions(self):
        results = []
        for action in self._actions:
            results.append(action.execute())
        return results

    def setTime(self, time):
        self._time = TimeString(time)
