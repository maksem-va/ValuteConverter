import unittest
from main import conv_money, cb_page_getter


class TestConv(unittest.TestCase):
    def test_value_type(self):
        self.assertTrue(isinstance(conv_money("usd", 1), float))

    def test_valute_value(self):
        self.assertTrue(conv_money("GBP", 1) >= 0)
