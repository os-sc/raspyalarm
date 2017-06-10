import unittest
from alarmconfig.actions.action import Action


class ActionTestCase(unittest.TestCase):
    def test_requirements_satisfied_returns_true_when_requirements_are_satisfied(self):
        a = Action('test action')
        a._requirements = ['req1', 'req2', 'req3']
        a.set_settings({'req1': 'value', 'req2': 123, 'req3': False})
        self.assertTrue(a.requirements_satisfied())

    def test_requirements_satisfied_returns_true_when_requirements_are_complete_but_none(self):
        a = Action('test action')
        a._requirements = ['req1', 'req2', 'req3']
        a.set_settings({'req1': None, 'req2': None, 'req3': None})
        self.assertTrue(a.requirements_satisfied())

    def test_requirements_satisfied_returns_false_when_requirements_are_not_satisfied(self):
        a = Action('test action')
        a._requirements = ['req1', 'req2', 'req3']
        self.assertFalse(a.requirements_satisfied())

    def test_requirements_satisfied_returns_false_when_requirements_are_not_complete_satisfied(self):
        a = Action('test action')
        a._requirements = ['req1', 'req2', 'req3']
        a.set_settings({'req1': 'value', 'req2': 123})
        self.assertFalse(a.requirements_satisfied())
