from collections import namedtuple

BUY = 'buy'
SELL = 'sell'

Trade = namedtuple("Trade", ['symbol', 'quantity', 'price', 'trade_type', 'timestamp'])

class DataStore(object):
    def __init__(self):
        self.entries = []

    @property
    def count(self):
        return len(self.entries)

    def append(self, entry):
        self.entries.append(entry)

    def find(self, symbol, timestamp=None):
        def _compare(e):
            if e.symbol == symbol:
                if timestamp:
                    return e.timestamp >= timestamp
                else:
                    return True
            return False

        return filter(_compare, self.entries)