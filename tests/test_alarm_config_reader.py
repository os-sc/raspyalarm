import unittest

from alarmconfig.alarm_config_reader import AlarmConfigReader
from alarmconfig.config_settings import ConfigSettings as CS
from alarmconfig.errors.config_error import ConfigError


class AlarmConfigReaderTestsCase(unittest.TestCase):
    #################
    # parse_configs #
    #################

    def test_empty_string_returns_empty_list(self):
        actual = AlarmConfigReader.parse_configs('')
        self.assertEqual(0, len(actual))

    def test_empty_object_string_returns_empty_list(self):
        actual = AlarmConfigReader.parse_configs('{}')
        self.assertEqual(0, len(actual))

    def test_empty_configuration_list_returns_empty_list(self):
        json = '{"' + CS.ConfigList + '": []}'
        actual = AlarmConfigReader.parse_configs(json)
        self.assertEqual(0, len(actual))

    def test_config_with_empty_configuration_raises_error(self):
        json = '{"' + CS.ConfigList + '": [{}]}'
        self.assertRaises(ConfigError, AlarmConfigReader.parse_configs, json)

    def test_config_with_empty_name_raises_error(self):
        json = '{"' + CS.ConfigList + '": [{"' + CS.ConfigName + '": "", "' + CS.EventGroupList + '": []}]}'
        self.assertRaises(ConfigError, AlarmConfigReader.parse_configs, json)

    def test_config_with_empty_event_group(self):
        json = '{"' + CS.ConfigList + '": [{"' + CS.ConfigName + '": "n", "' \
               + CS.EventGroupList + '": []}]}'
        actual = AlarmConfigReader.parse_configs(json)[0]._eventGroups
        self.assertEqual(0, len(actual))

    def test_config_with_empty_event_list(self):
        json = '{"' + CS.ConfigList + '": [{"' + CS.ConfigName + '": "n", "' \
               + CS.EventGroupList + '": [{"' + CS.EventGroupName + '": "eg", "' + CS.EventList + '": []}]}]}'
        actual = AlarmConfigReader.parse_configs(json)[0]._eventGroups[0]._events
        self.assertEqual(0, len(actual))

    def test_config_with_empty_event_time_raises_error(self):
        json = '{"' + CS.ConfigList + '": [{"' + CS.ConfigName + '": "n", "' \
               + CS.EventGroupList + '": [{"' + CS.EventGroupName + '": "eg", "' + CS.EventList \
               + '": [{"' + CS.EventName + '": "e", "' + CS.EventTime + '": ""}]}]}]}'
        self.assertRaises(ConfigError, AlarmConfigReader.parse_configs, json)

    def test_config_with_empty_event_name_raises_error(self):
        json = '{"' + CS.ConfigList + '": [{"' + CS.ConfigName + '": "n", "' \
               + CS.EventGroupList + '": [{"' + CS.EventGroupName + '": "eg", "' + CS.EventList \
               + '": [{"' + CS.EventName + '": "", "' + CS.EventTime + '": "0815"}]}]}]}'
        self.assertRaises(ConfigError, AlarmConfigReader.parse_configs, json)

    def test_config_with_event(self):
        json = '{"' + CS.ConfigList + '": [{"' + CS.ConfigName + '": "n", "' \
               + CS.EventGroupList + '": [{"' + CS.EventGroupName + '": "eg", "' + CS.EventList \
               + '": [{"' + CS.EventName + '": "e", "' + CS.EventTime + '": "0815"}]}]}]}'
        actual = AlarmConfigReader.parse_configs(json)[0]._eventGroups[0]._events
        self.assertEqual(1, len(actual))
