from alarmconfig.events.event import Event
from alarmconfig.repeaters.repeater import Repeater

class EventGroup():
    def __init__(self, name):
        if not name:
            raise ValueError('Name cannot be empty for EventGroup')
        self.name = name
        self._events = []
        self._repeaters = []

    def add_event(self, event):
        if not isinstance(event, Event):
            raise TypeError('Events can only contain items of type Event, got ' + str(type(event)))
        for e in self._events:
            if e.name == event.name:
                raise ValueError('Event with name already exists: ' + e.name)
        self._events.append(event)

    def add_repeater(self, repeater):
        if not isinstance(repeater, Repeater):
            raise TypeError('Repeaters can only contain items of type Repeater, got ' + str(type(repeater)))
        self._repeaters.append(repeater)
