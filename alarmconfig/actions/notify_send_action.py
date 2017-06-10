from subprocess import run
from alarmconfig.actions.action import Action
from alarmconfig.errors.action_settings_error import ActionSettingsError


class NotifySendAction(Action):
    def __init__(self, name):
        super().__init__(name)

    def _execute(self):
        result = run(['notify-send', self._settings['notify-message']])
        return True if result.returncode == 0 else False
