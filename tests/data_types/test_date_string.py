import unittest
from datetime import datetime
from alarmconfig.data_types.date_string import DateString


class DateStringTestsCase(unittest.TestCase):
    def SetUp(self):
        pass

        ##########################
        # TestString Constructor #
        ##########################

    def test_initializing_date_string_with_int_0_returns_00000000(self):
        expected = '00000000'
        ts = DateString(0)
        actual = str(ts)

        self.assertEqual(expected, actual)

    def test_initializing_date_string_with_int_31122000_returns_31122000(self):
        expected = '31122000'
        ts = DateString(31122000)
        actual = str(ts)

        self.assertEqual(expected, actual)

    def test_initializing_date_string_with_str_0_returns_00000000(self):
        expected = '00000000'
        ts = DateString('0')
        actual = str(ts)

        self.assertEqual(expected, actual)

    def test_initializing_date_string_with_str_31122000_returns_31122000(self):
        expected = '31122000'
        ts = DateString('31122000')
        actual = str(ts)

        self.assertEqual(expected, actual)

    def test_initializing_date_string_with_int_32000000_raises_error(self):
        self.assertRaises(ValueError, DateString, 32000000)

    def test_initializing_date_string_with_str_00130000_raises_error(self):
        self.assertRaises(ValueError, DateString, '32000000')

    def test_initializing_date_string_with_int_130000_raises_error(self):
        self.assertRaises(ValueError, DateString, 130000)

    def test_initializing_date_string_with_str_130000_raises_error(self):
        self.assertRaises(ValueError, DateString, '130000')

    def test_initializing_date_string_with_int_minus1_raises_error(self):
        self.assertRaises(ValueError, DateString, -1)

    def test_initializing_date_string_with_str_minus1_raises_error(self):
        self.assertRaises(ValueError, DateString, '-1')

    def test_initializing_with_a_bool_raises_error(self):
        self.assertRaises(TypeError, DateString, True)

    ######################
    # DateString Getters #
    ######################

    def test_day_returns_correct_digits(self):
        expected = 12
        ds = DateString('01011970')
        ds._string = '12345678'
        actual = ds.day
        self.assertEqual(expected, actual)

    def test_month_returns_correct_digits(self):
        expected = 34
        ds = DateString('01011970')
        ds._string = '12345678'
        actual = ds.month
        self.assertEqual(expected, actual)

    def test_year_returns_correct_digits(self):
        expected = 5678
        ds = DateString('01011970')
        ds._string = '12345678'
        actual = ds.year
        self.assertEqual(expected, actual)

    #######################
    # DateString.left_pad #
    #######################

    def test_leftpad_0_returns_0000(self):
        expected = '00000000'
        actual = DateString.left_pad('0')

        self.assertEqual(expected, actual)

    def test_leftpad_4_returns_00000004(self):
        expected = '00000004'
        actual = DateString.left_pad('4')

        self.assertEqual(expected, actual)

    def test_leftpad_34_returns_00000034(self):
        expected = '00000034'
        actual = DateString.left_pad('34')

        self.assertEqual(expected, actual)

    def test_leftpad_234_returns_00000234(self):
        expected = '00000234'
        actual = DateString.left_pad('234')

        self.assertEqual(expected, actual)

    def test_leftpad_1234_returns_00001234(self):
        expected = '00001234'
        actual = DateString.left_pad('1234')

        self.assertEqual(expected, actual)

    def test_leftpad_12345_returns_00012345(self):
        expected = '00012345'
        actual = DateString.left_pad('12345')

        self.assertEqual(expected, actual)

    def test_leftpad_123456_returns_00123456(self):
        expected = '00123456'
        actual = DateString.left_pad('123456')

        self.assertEqual(expected, actual)

    def test_leftpad_1234567_returns_01234567(self):
        expected = '01234567'
        actual = DateString.left_pad('1234567')

        self.assertEqual(expected, actual)

    def test_leftpad_12345678_returns_12345678(self):
        expected = '12345678'
        actual = DateString.left_pad('12345678')

        self.assertEqual(expected, actual)

    def test_leftpad_123456789_returns_123456789(self):
        expected = '123456789'
        actual = DateString.left_pad('123456789')

        self.assertEqual(expected, actual)

    def test_leftpad_leetleet_returns_leetleet(self):
        expected = 'leetleet'
        actual = DateString.left_pad('leetleet')

        self.assertEqual(expected, actual)

    def test_leftpad_minus1_returns_000000minus1(self):
        expected = '000000-1'
        actual = DateString.left_pad('-1')

        self.assertEqual(expected, actual)

    ###################################
    # DateString.is_valid_date_string #
    ###################################

    def test_00000000_is_valid_date_string(self):
        self.assertTrue(DateString.is_valid_date_string('00000000'))

    def test_01010001_is_valid_date_string(self):
        self.assertTrue(DateString.is_valid_date_string('01010001'))

    def test_0000000_is_not_a_valid_date_string(self):
        self.assertFalse(DateString.is_valid_date_string('0000000'))

    def test_000000000_is_valid_date_string(self):
        self.assertFalse(DateString.is_valid_date_string('000000000'))

    def test_31120000_is_valid_date_string(self):
        self.assertTrue(DateString.is_valid_date_string('31120000'))

    def test_32000000_is_valid_date_string(self):
        self.assertFalse(DateString.is_valid_date_string('32000000'))

    def test_00130000_is_valid_date_string(self):
        self.assertFalse(DateString.is_valid_date_string('00130000'))

    def test_00001970_is_valid_date_string(self):
        self.assertTrue(DateString.is_valid_date_string('00001970'))

    def test_00002015_is_valid_date_string(self):
        self.assertTrue(DateString.is_valid_date_string('00002015'))

    def test_00002222_is_valid_date_string(self):
        self.assertTrue(DateString.is_valid_date_string('00002222'))

    def test_00009999_is_valid_date_string(self):
        self.assertTrue(DateString.is_valid_date_string('00009999'))

    def test_0x000000_is_not_a_valid_date_string(self):
        self.assertFalse(DateString.is_valid_date_string('0x000000'))

    def test_minus1_is_not_a_valid_date_string(self):
        self.assertFalse(DateString.is_valid_date_string('-1'))

    ###########################
    # DateString compare_with #
    ###########################

    def test_comparing_date_string_with_same_datetime_returns_true(self):
        dates = {
            '31122999': datetime(year=2999, month=12, day=31),
            '01011900': datetime(year=1900, month=1, day=1)
        }
        for s, dt in dates.items():
            self.assertTrue(DateString(s).compare_with_datetime(dt))

    def test_comparing_date_string_with_past_datetime_returns_false(self):
        dates = {
            '31122999': datetime(year=2999, month=12, day=30),
            '01011900': datetime(year=1899, month=1, day=1)
        }
        for s, dt in dates.items():
            self.assertFalse(DateString(s).compare_with_datetime(dt))

    def test_comparing_date_string_with_future_datetime_returns_false(self):
        dates = {
            '30122999': datetime(year=2999, month=12, day=31),
            '01011899': datetime(year=1900, month=1, day=1)
        }
        for s, dt in dates.items():
            self.assertFalse(DateString(s).compare_with_datetime(dt))

    def test_comparing_date_string_with_same_date_string_returns_true(self):
        dates = {
            '31122999': DateString('31122999'),
            '01011900': DateString('01011900')
        }
        for s, ds in dates.items():
            self.assertTrue(DateString(s).compare_with(ds))

    def test_comparing_date_string_with_past_date_string_returns_false(self):
        dates = {
            '31122999': DateString('3012299'),
            '01011900': DateString('01011899')
        }
        for s, ds in dates.items():
            self.assertFalse(DateString(s).compare_with(ds))

    def test_comparing_date_string_with_future_date_string_returns_false(self):
        dates = {
            '30122999': DateString('31122999'),
            '01011899': DateString('01011900')
        }
        for s, ds in dates.items():
            self.assertFalse(DateString(s).compare_with(ds))

    def test_comparing_date_string_with_same_string_returns_true(self):
        dates = {
            '31122999': '31122999',
            '01011900': '01011900'
        }
        for s, string in dates.items():
            self.assertTrue(DateString(s).compare_with_string(string))

    def test_comparing_date_string_with_past_string_returns_false(self):
        dates = {
            '31122999': '3012299',
            '01011900': '01011899'
        }
        for s, string in dates.items():
            self.assertFalse(DateString(s).compare_with_string(string))

    def test_comparing_date_string_with_future_string_returns_false(self):
        dates = {
            '30122999': '31122999',
            '01011899': '01011900'
        }
        for s, string in dates.items():
            self.assertFalse(DateString(s).compare_with_string(string))

    ####################################
    # DateString.convert_from_datetime #
    ####################################

    def test_01011970_converts_correct(self):
        expected = '01011900'
        actual = DateString.convert_from_datetime(datetime(year=1900, month=1, day=1))
        self.assertEqual(expected, str(actual))

    def test_31122999_converts_correct(self):
        expected = '31122999'
        actual = DateString.convert_from_datetime(datetime(year=2999, month=12, day=31))
        self.assertEqual(expected, str(actual))
