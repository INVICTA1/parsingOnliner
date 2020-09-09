import unittest
from test import parse_date
from datetime import datetime, date, time, timedelta

actual_date_time = datetime.strptime("20/8/25 16:30:00", "%y/%m/%d %H:%M:%S")

class OnlinerTest(unittest.TestCase):

    def test_parse_date(self):
        self.assertEqual(parse_date(actual_date_time, '1 секунду назад'),
                             str(actual_date_time - timedelta(seconds=1)))  # time
        # self.assertEquals(parse_date(ACTUAL_DATE_TIME, '2 секунды назад'), ACTUAL_DATE    _TIME - timedelta(seconds=2))
        # self.assertEquals(parse_date(ACTUAL_DATE_TIME, '5 секунд назад'), ACTUAL_DATE_TIME - timedelta(seconds=5))
        # self.assertEquals(parse_date('1 минуту назад'), "time")
        # self.assertEquals(parse_date('2 минуты назад'), "time")
        # self.assertEquals(parse_date('5 минут назад'), "time")
        # self.assertEquals(parse_date('1 час назад'), "time")
        # self.assertEquals(parse_date('2 часа назад'), "time")
        # self.assertEquals(parse_date('5 часов назад'), "time")
        # self.assertEquals(parse_date('1 день назад'), "time")
        # self.assertEquals(parse_date('2 дня назад'), "time")
        # self.assertEquals(parse_date('5 дней назад'), "time")
