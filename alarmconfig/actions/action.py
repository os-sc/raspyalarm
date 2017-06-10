class Action:
    """ Static base class """
    def __init__(self, name):
        self.name = name
        self._settings = {}
        self._requirements = []

    def execute(self):
        if not self.requirements_satisfied():
            raise ActionSettingsError('Tried executing action without valid settings')
        return self._execute()

    def _execute(self):
        raise NotImplementedError('Non implemented base class method has been called')

    def set_settings(self, settings):
        for k, v in settings.items():
            self._settings[k] = v

    def requirements_satisfied(self):
        for r in self._requirements:
            if r not in self._settings:
                return False
        return True
