import unittest

from alarmconfig.alarm_config import AlarmConfig
from alarmconfig.events.event_group import EventGroup

class AlarmConfigTestCase(unittest.TestCase):
    def SetUp(self):
        pass

    def test_initialize_config_name(self):
        expected = 'SuperCoolEventName'
        actual = AlarmConfig(expected).name
        self.assertEqual(actual, expected)

    def test_initialize_config_with_whitespace_as_name(self):
        expected = ' '
        actual = AlarmConfig(expected).name
        self.assertEqual(actual, expected)

    def test_initialize_event_with_empty_name_raises_error(self):
        self.assertRaises(ValueError, AlarmConfig, '')

    ##################
    # EventGroup.add #
    ##################

    def test_alarmconfig_add_eventgroup(self):
        ac = AlarmConfig('test config')
        ac.add_event_group(EventGroup('e'))
        self.assertEqual(1, len(ac._eventGroups))

    def test_alarmconfig_add_alarmconfig_raises_error(self):
        ac = AlarmConfig('test config')
        self.assertRaises(TypeError, ac.add_event_group, ac)
