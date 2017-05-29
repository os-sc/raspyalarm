import json

from alarmconfig.events.event_group import EventGroup

from alarmconfig.alarm_config import AlarmConfig
from alarmconfig.config_settings import ConfigSettings as CS
from alarmconfig.errors.config_error import ConfigError
from alarmconfig.events.event import Event

class AlarmConfigReader():
    @staticmethod
    def parse_configs(string: str):
        try:
            configs = []
            if len(string) == 0:
                return configs

            j = json.loads(string)
            if CS.ConfigList not in j:
                return configs

            assert len(j[CS.ConfigList]) >= 0
            for cfg in j[CS.ConfigList]:
                assert cfg[CS.ConfigName]
                assert len(cfg[CS.EventGroupList]) >= 0
                config = AlarmConfig(cfg[CS.ConfigName])
                configs.append(config)

                for eg in cfg[CS.EventGroupList]:
                    assert eg[CS.EventGroupName]
                    assert len(eg[CS.EventList]) >= 0
                    event_group = EventGroup(eg[CS.EventGroupName])
                    config.add_event_group(event_group)

                    for e in eg[CS.EventList]:
                        assert e[CS.EventName]
                        assert e[CS.EventTime]
                        event = Event(e[CS.EventName])
                        event.setTime(e[CS.EventTime])
                        event_group.add_event(event)
            return configs
        except AssertionError as e:
            raise ConfigError('Missing key in configuration') from e
        except KeyError as e:
            raise ConfigError('Could not find key: ' + str(type(e)) + ' ' + str(e)) from e
        except json.JSONDecodeError as e:
            raise ConfigError('Could not parse config, invalid JSON: ' + str(e)) from e
        except Exception as e:
            raise ConfigError('An error occurred when parsing the config: ' + str(type(e)) + ' ' + str(e)) from e