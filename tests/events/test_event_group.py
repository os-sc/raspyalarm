import unittest

from alarmconfig.events.event import Event
from alarmconfig.events.event_group import EventGroup
from alarmconfig.repeaters.repeater import Repeater
from alarmconfig.repeaters.single_date_repeater import SingleDateRepeater


class EventGroupTestCase(unittest.TestCase):
    def SetUp(self):
        pass

    ##########################
    # EventGroup Constructor #
    ##########################

    def test_initialize_eventgroup_name(self):
        expected = 'SuperCoolEventName'
        actual = EventGroup(expected).name
        self.assertEqual(actual, expected)

    def test_initialize_eventgroup_with_whitespace_as_name(self):
        expected = ' '
        actual = EventGroup(expected).name
        self.assertEqual(actual, expected)

    def test_initialize_eventgroup_with_empty_name_raises_error(self):
        self.assertRaises(ValueError, EventGroup, '')

    ########################
    # EventGroup.add_event #
    ########################

    def test_eventgroup_add_event(self):
        eg = EventGroup('test group')
        eg.add_event(Event('e'))
        self.assertEqual(1, len(eg._events))

    def test_eventgroup_add_repeater_to_events_raises_error(self):
        eg = EventGroup('test group')
        self.assertRaises(TypeError, eg.add_event, Repeater())

    def test_eventgroup_add_event_twice_raises_error(self):
        eg = EventGroup('test group')
        e = Event('e')
        eg.add_event(e)
        self.assertRaises(ValueError, eg.add_event, e)

    ###########################
    # EventGroup.add_repeater #
    ###########################

    def test_eventgroup_add_single_date_repeater(self):
        eg = EventGroup('test group')
        eg.add_repeater(SingleDateRepeater())
        self.assertEqual(1, len(eg._repeaters))

    def test_eventgroup_add_event_to_repeaters_raises_error(self):
        eg = EventGroup('test group')
        self.assertRaises(TypeError, eg.add_repeater, eg)

    def test_eventgroup_add_repeater_twice_has_two_repeaters(self):
        expected = 2
        eg = EventGroup('test group')
        r = Repeater()
        eg.add_repeater(r)
        eg.add_repeater(r)
        actual = eg._repeaters
        self.assertEqual(expected, len(actual))
