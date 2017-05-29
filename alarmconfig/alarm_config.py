from alarmconfig.events.event_group import EventGroup


class AlarmConfig():
    def __init__(self, name: str):
        if not name:
            raise ValueError('Name cannot be empty for AlarmConfig')
        self.name = name
        self._eventGroups = []

    def add_event_group(self, eg):
        if not isinstance(eg, EventGroup):
            raise TypeError('add_event_group only accepts items of type EventGroup, got ' + str(type(eg)))
        for group in self._eventGroups:
            if group.name == eg.name:
                raise ValueError('EventGroup with name already exists: ' + eg.name)
        self._eventGroups.append(eg)
