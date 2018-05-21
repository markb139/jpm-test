import unittest
from datetime import datetime, timedelta

from gbce.datastore import Trade, BUY, SELL
from gbce.model import GBCEModel, default_model
from gbce.stocks import CommonStock, PreferredStock


class TestModel(unittest.TestCase):
    def setUp(self):
        stock_entries = {
            "common": CommonStock(last_dividend=10, par_value=10),
            "preferred": PreferredStock(last_dividend=1.0, par_value=100, fixed_dividend=0.1)
        }
        self.model = GBCEModel(stock_entries=stock_entries)
        self.assertIsNotNone(self.model)

    def test_calc_yield(self):
        dividend_yield = self.model.dividend_yield(symbol="common", price=10.0)
        self.assertEqual(dividend_yield, 1.0)

        dividend_yield = self.model.dividend_yield(symbol="preferred", price=1.0)
        self.assertEqual(dividend_yield, 10.0)

    def test_calc_pe_ratio(self):
        pe_ratio = self.model.pe_ratio(symbol="common", price=10.0)
        self.assertEqual(pe_ratio, 1.0)
        pe_ratio = self.model.pe_ratio(symbol="preferred", price=10.0)
        self.assertEqual(pe_ratio, 10.0)

    def test_record_buy_trade(self):
        new_entry = Trade(symbol="common", quantity=100, price=100.0, trade_type=BUY, timestamp=datetime.utcnow())
        self.model.record(new_entry)
        self.assertEqual(self.model.count, 1)

    def test_record_sell_trade(self):
        new_entry = Trade(symbol="common", quantity=100, price=100.0, trade_type=SELL, timestamp=datetime.utcnow())
        self.model.record(new_entry)
        self.assertEqual(self.model.count, 1)

    def test_volume_weighted_price(self):
        now = datetime.utcnow()
        for t in range(1,5):
            entry = Trade(symbol="common", quantity=100, price=100.0, trade_type=BUY,
                          timestamp=now - timedelta(minutes=t))
            self.model.record(entry)

        very_old_entry = Trade(symbol="common", quantity=100, price=200.0, trade_type=BUY,
                               timestamp=now - timedelta(minutes=6))
        self.model.record(very_old_entry)

        volume_weighted_price = self.model.volume_weighted_price(symbol="common")
        self.assertEqual(volume_weighted_price, 100.0)

    def test_all_share_index(self):
        now = datetime.utcnow()
        entry = Trade(symbol="common", quantity=1, price=100.0, trade_type=BUY, timestamp=now)
        self.model.record(entry)
        entry = Trade(symbol="preferred", quantity=1, price=4.0, trade_type=BUY, timestamp=now)
        self.model.record(entry)

        all_share_index = self.model.all_share_index()
        self.assertEqual(all_share_index, 20.0)

    def test_default_model(self):
        now = datetime.utcnow()
        for symbol in ['TEA', 'POP', 'ALE', 'GIN', 'JOE']:
            entry = Trade(symbol=symbol, quantity=1, price=2.0, trade_type=BUY, timestamp=now)
            default_model.record(entry)

        all_share_index = default_model.all_share_index()
        self.assertEqual(all_share_index, 2.0)
