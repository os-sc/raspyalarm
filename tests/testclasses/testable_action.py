from alarmconfig.actions.action import Action


class TestableAction(Action):
    def __init__(self):
        super().__init__()

    def execute(self):
        return self._settings['result']
