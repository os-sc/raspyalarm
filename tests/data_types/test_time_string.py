import unittest

from alarmconfig.data_types.time_string import TimeString

class TimeStringTestsCase(unittest.TestCase):
    def SetUp(self):
        pass

    ##########################
    # TestString Constructor #
    ##########################

    def test_initializing_timestring_with_int_0_returns_0000(self):
        expected = '0000'
        ts = TimeString(0)
        actual = str(ts)

        self.assertEqual(expected, actual)

    def test_initializing_timestring_with_int_2359_returns_2359(self):
        expected = '2359'
        ts = TimeString(2359)
        actual = str(ts)

        self.assertEqual(expected, actual)

    def test_initializing_timestring_with_str_0_returns_0000(self):
        expected = '0000'
        ts = TimeString('0')
        actual = str(ts)

        self.assertEqual(expected, actual)

    def test_initializing_timestring_with_str_2359_returns_2359(self):
        expected = '2359'
        ts = TimeString('2359')
        actual = str(ts)

        self.assertEqual(expected, actual)

    def test_initializing_timestring_with_int_2400_raises_error(self):
        self.assertRaises(ValueError, TimeString, 2400)

    def test_initializing_timestring_with_str_2400_raises_error(self):
        self.assertRaises(ValueError, TimeString, '2400')

    def test_initializing_timestring_with_int_minus1_raises_error(self):
        self.assertRaises(ValueError, TimeString, -1)

    def test_initializing_timestring_with_str_minus1_raises_error(self):
        self.assertRaises(ValueError, TimeString, '-1')

    def test_initializing_with_a_bool_raises_error(self):
        self.assertRaises(TypeError, TimeString, True)

    #######################
    # TestString.left_pad #
    #######################

    def test_leftpad_0_returns_0000(self):
        expected = '0000'
        actual = TimeString.left_pad('0')

        self.assertEqual(expected, actual)

    def test_leftpad_4_returns_0004(self):
        expected = '0004'
        actual = TimeString.left_pad('4')

        self.assertEqual(expected, actual)

    def test_leftpad_34_returns_0034(self):
        expected = '0034'
        actual = TimeString.left_pad('34')

        self.assertEqual(expected, actual)

    def test_leftpad_234_returns_0234(self):
        expected = '0234'
        actual = TimeString.left_pad('234')

        self.assertEqual(expected, actual)

    def test_leftpad_1234_returns_1234(self):
        expected = '1234'
        actual = TimeString.left_pad('1234')

        self.assertEqual(expected, actual)

    def test_leftpad_01234_returns_01234(self):
        expected = '01234'
        actual = TimeString.left_pad('01234')

        self.assertEqual(expected, actual)

    def test_leftpad_leet_returns_leet(self):
        expected = 'leet'
        actual = TimeString.left_pad('leet')

        self.assertEqual(expected, actual)

    def test_leftpad_minus1_returns_00minus1(self):
        expected = '00-1'
        actual = TimeString.left_pad('-1')

        self.assertEqual(expected, actual)

    ##################################
    # TimeString.is_valid_timestring #
    ##################################

    def test_0000_is_valid_timestring(self):
        self.assertTrue(TimeString.is_valid_time_string('0000'))

    def test_0059_is_valid_timestring(self):
        self.assertTrue(TimeString.is_valid_time_string('0059'))

    def test_1337_is_valid_timestring(self):
        self.assertTrue(TimeString.is_valid_time_string('1337'))

    def test_2359_is_valid_timestring(self):
        self.assertTrue(TimeString.is_valid_time_string('2359'))

    def test_0060_is_not_valid_timestring(self):
        self.assertFalse(TimeString.is_valid_time_string('0060'))

    def test_9999_is_not_valid_timestring(self):
        self.assertFalse(TimeString.is_valid_time_string('9999'))

    def test_leet_is_not_valid_timestring(self):
        self.assertFalse(TimeString.is_valid_time_string('leet'))

    def test_2459_is_not_valid_timestring(self):
        self.assertFalse(TimeString.is_valid_time_string('2459'))

    def test_2400_is_not_valid_timestring(self):
        self.assertFalse(TimeString.is_valid_time_string('2400'))

    def test_00minus1_is_not_valid_timestring(self):
        self.assertFalse(TimeString.is_valid_time_string('00-1'))

    def test_01337_is_not_valid_timestring(self):
        self.assertFalse(TimeString.is_valid_time_string('01337'))

    def test_0dot01_is_not_valid_timestring(self):
        self.assertFalse(TimeString.is_valid_time_string('0.01'))

    def test_0x05_is_not_valid_timestring(self):
        self.assertFalse(TimeString.is_valid_time_string('0x05'))

    def test_int_7_is_not_valid_timestring(self):
        self.assertFalse(TimeString.is_valid_time_string(7))