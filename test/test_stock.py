import unittest

from gbce.stocks import CommonStock, PreferredStock


class CommonStockTest(unittest.TestCase):
    def setUp(self):
        self.stock = CommonStock(last_dividend=1.0, par_value=100)
        self.assertIsNotNone(self.stock)

    def test_dividend_yield(self):
        dividend_yield = self.stock.dividend_yield(price=1.0)
        self.assertEqual(dividend_yield, 1.0)

    def test_pe_ratio(self):
        pe_ratio = self.stock.pe_ratio(price=1.0)
        self.assertEqual(pe_ratio, 1.0)


class PreferredStockTest(unittest.TestCase):
    def setUp(self):
        self.stock = PreferredStock(last_dividend=1.0, fixed_dividend=0.1, par_value=100)
        self.assertIsNotNone(self.stock)

    def test_dividend_yield(self):
        dividend_yield = self.stock.dividend_yield(price=1.0)
        self.assertEqual(dividend_yield, 10.0)
