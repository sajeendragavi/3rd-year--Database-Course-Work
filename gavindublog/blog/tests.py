from datetime import date
from unittest.mock import patch


from django.test import TestCase


from blog.function import myfunc_using_date

def mocked_today():
    return date(year=2021, month=1, day=1)

class TestImmutableObject(TestCase):
    @patch("blog.function.get_today", mocked_today)
    def test_myfunc_using_date(self):
        self.assertEqual(myfunc_using_date().strftime("%Y-%m-%d"), "2021-01-01")
# Create your tests here.
