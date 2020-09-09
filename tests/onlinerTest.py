import unittest
from parse.test import parse_date
from datetime import datetime, timedelta

actual_date_time = datetime.strptime("20/8/25 16:30:00", "%y/%m/%d %H:%M:%S")


class OnlinerTest(unittest.TestCase):

    def test_parse_date(self):
        self.assertEqual(parse_date(actual_date_time, '1 секунду назад'), str(actual_date_time - timedelta(seconds=1)))
        self.assertEqual(parse_date(actual_date_time, '2 секунды назад'), str(actual_date_time - timedelta(seconds=2)))
        self.assertEqual(parse_date(actual_date_time, '5 секунд назад'), str(actual_date_time - timedelta(seconds=5)))
        self.assertEqual(parse_date(actual_date_time, '1 минуту назад'), str(actual_date_time - timedelta(minutes=1)))
        self.assertEqual(parse_date(actual_date_time, '2 минуты назад'), str(actual_date_time - timedelta(minutes=2)))
        self.assertEqual(parse_date(actual_date_time, '5 минут назад'), str(actual_date_time - timedelta(minutes=5)))
        self.assertEqual(parse_date(actual_date_time, '1 час назад'), str(actual_date_time - timedelta(hours=1)))
        self.assertEqual(parse_date(actual_date_time, '2 часа назад'), str(actual_date_time - timedelta(hours=2)))
        self.assertEqual(parse_date(actual_date_time, '5 часов назад'), str(actual_date_time - timedelta(hours=5)))
        self.assertEqual(parse_date(actual_date_time, '1 день назад'), str(actual_date_time - timedelta(days=1)))
        self.assertEqual(parse_date(actual_date_time, '2 дня назад'), str(actual_date_time - timedelta(days=2)))
        self.assertEqual(parse_date(actual_date_time, '5 дней назад'), str(actual_date_time - timedelta(days=5)))
