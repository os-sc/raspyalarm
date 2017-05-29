import unittest

from alarmconfig.events.event import Event

class EventTestCase(unittest.TestCase):
    def SetUp(self):
        pass

    def test_initialize_event_name(self):
        expected = 'SuperCoolEventName'
        actual = Event(expected).name
        self.assertEqual(actual, expected)

    def test_initialize_event_with_whitespace_as_name(self):
        expected = ' '
        actual = Event(expected).name
        self.assertEqual(actual, expected)

    def test_initialize_event_with_empty_name_raises_error(self):
        self.assertRaises(ValueError, Event, '')

