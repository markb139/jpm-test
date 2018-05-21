from collections import namedtuple

BUY = 'buy'
SELL = 'sell'

Trade = namedtuple("Trade", ['symbol', 'quantity', 'price', 'trade_type', 'timestamp'])

class DataStore(object):
    """In memory data store"""
    def __init__(self):
        self.entries = []

    @property
    def count(self):
        return len(self.entries)

    def append(self, entry):
        """Append a new entry to the database"""
        self.entries.append(entry)

    def find(self, symbol, timestamp=None):
        """Find entries
        :param str symbol: stock symbol to find
        :param datetime timestamp: optional time to filter on
        :return: list of trades
        """
        def _compare(e):
            if e.symbol == symbol:
                if timestamp:
                    return e.timestamp >= timestamp
                else:
                    return True
            return False

        return filter(_compare, self.entries)