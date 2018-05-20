import unittest

from gbce.formulas import calc_pe_ratio, calc_geometric_mean, calc_volume_weighted_stock_price, \
    calc_common_dividend_yield, calc_preferred_dividend_yield


class CommonDividendYieldTest(unittest.TestCase):
    def test_calc_yield(self):
        last_dividend = 10.0
        price = 2.0
        dividend_yield = calc_common_dividend_yield(last_dividend=last_dividend, price=price)
        self.assertEquals(dividend_yield, 5.0)


class PreferredDividendYieldTest(unittest.TestCase):
    def test_calc_yield(self):
        dividend = 10.0
        par_value = 10.0
        price = 2.0
        dividend_yield = calc_preferred_dividend_yield(dividend=dividend, par_value=par_value, price=price)
        self.assertEquals(dividend_yield, 50.0)


class PERationTest(unittest.TestCase):
    def test_calc_pe_ratio(self):
        price = 1.0
        dividend = 1.0
        pe_ratio = calc_pe_ratio(price=price, dividend=dividend)
        self.assertEquals(pe_ratio, 1.0)


class GeometricMeanTest(unittest.TestCase):
    def test_calc_geometric_mean_for_empty_list(self):
        prices = []
        mean = calc_geometric_mean(prices=prices)
        self.assertEquals(mean, 1.0)

    def test_calc_geometric_mean_for_single_value(self):
        prices = [1.0]
        mean = calc_geometric_mean(prices=prices)
        self.assertEquals(mean, 1.0)

    def test_calc_geometric_mean_for_multiple_values(self):
        prices = [2.0, 8.0]
        mean = calc_geometric_mean(prices=prices)
        self.assertEquals(mean, 4.0)


class VolumeWeightedStockPriceTest(unittest.TestCase):
    def test_calc_volume_weighted_stock_price_for_empty_list(self):
        trades = []
        stock_price = calc_volume_weighted_stock_price(trades=trades)
        self.assertEquals(stock_price, 0.0)

    def test_calc_volume_weighted_stock_price_for_single_trade(self):
        trades = [(1.0, 100)]
        stock_price = calc_volume_weighted_stock_price(trades=trades)
        self.assertEquals(stock_price, 1.0)

    def test_calc_volume_weighted_stock_price_for_multiple_trades(self):
        trades = [(10.0, 100), (30.0, 300)]
        stock_price = calc_volume_weighted_stock_price(trades=trades)
        self.assertEquals(stock_price, 25.0)
