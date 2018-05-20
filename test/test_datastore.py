import unittest
from datetime import datetime, timedelta

from gbce.datastore import DataStore, Trade, BUY


class TestDataStore(unittest.TestCase):
    def test_create_data_store(self):
        d = DataStore()
        self.assertIsNotNone(d)

    def test_insert_entry(self):
        d = DataStore()
        new_entry = Trade(symbol="TEST", quantity=100, price=100.0, trade_type=BUY, timestamp=datetime.utcnow())
        d.append(new_entry)
        self.assertEqual(d.count, 1)

    def test_find_trade(self):
        d = DataStore()
        new_entry = Trade(symbol="TEST", quantity=100, price=100.0, trade_type=BUY, timestamp=datetime.utcnow())
        d.append(new_entry)

        entry = d.find(symbol="TEST")
        self.assertNotEquals(entry, [])

    def test_find_latest(self):
        d = DataStore()
        now = datetime.utcnow()
        new_entry = Trade(symbol="TEST", quantity=100, price=100.0, trade_type=BUY, timestamp=now)
        old_entry = Trade(symbol="TEST", quantity=100, price=1.0, trade_type=BUY, timestamp=now - timedelta(minutes=10))

        d.append(new_entry)
        d.append(old_entry)

        entries = d.find(symbol="TEST", timestamp=now - timedelta(minutes=5))
        expected = [Trade(symbol="TEST", quantity=100, price=100.0, trade_type=BUY, timestamp=now)]

        self.assertEquals(entries, expected)