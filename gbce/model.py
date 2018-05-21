from datetime import datetime, timedelta

from gbce.datastore import DataStore

from .formulas import calc_volume_weighted_stock_price, calc_geometric_mean
from .stocks import CommonStock, PreferredStock


class NoSuchStockException(Exception):
    pass


class GBCEModel(object):
    """GBCE model"""
    def __init__(self, stock_entries):
        self.entries = stock_entries
        self.store = DataStore()

    @property
    def count(self):
        return self.store.count

    def dividend_yield(self, symbol, price):
        """Calculate dividend yield
        :param str symbol: stock symbol
        :param float price: current price of stock
        :return: calculated yield
        """
        if symbol not in self.entries:
            raise NoSuchStockException()
        return self.entries[symbol].dividend_yield(price=price)

    def pe_ratio(self, symbol, price):
        """Calculate P/E ratio
        :param str symbol: stock symbol
        :param float price: current price of stock
        :return: calculated P/E ratio
        """
        if symbol not in self.entries:
            raise NoSuchStockException()
        return self.entries[symbol].pe_ratio(price=price)

    def volume_weighted_price(self, symbol):
        """Calculate volume weighted price of stock from the stored trades
        :param str symbol: stock symbol
        :return: calculated price
        """
        if symbol not in self.entries:
            raise NoSuchStockException()
        timestamp_filter = datetime.utcnow() - timedelta(minutes=5)
        trades = map(lambda e: (e.price, e.quantity), self.store.find(symbol=symbol, timestamp=timestamp_filter))
        return calc_volume_weighted_stock_price(trades=trades)

    def all_share_index(self):
        """Calculate the all share index value
        :return: calculated all share index value
        """
        timestamp_filter = datetime.utcnow() - timedelta(minutes=5)
        prices = []
        for symbol in self.entries.keys():
            trades = map(lambda e: (e.price, e.quantity), self.store.find(symbol=symbol, timestamp=timestamp_filter))
            if trades:
                prices.append(calc_volume_weighted_stock_price(trades=trades))
        return calc_geometric_mean(prices)

    def record(self, trade):
        """Record a new trade
        :param trade trade: the trade data to store
        """
        if trade.symbol not in self.entries:
            raise NoSuchStockException()
        self.store.append(trade)


default_stock_entries = {
    'TEA': CommonStock(last_dividend=0.0, par_value=100),
    'POP': CommonStock(last_dividend=8.0, par_value=100),
    'ALE': CommonStock(last_dividend=23.0, par_value=60),
    'GIN': PreferredStock(last_dividend=8.0, fixed_dividend=0.02, par_value=100),
    'JOE': CommonStock(last_dividend=13.0, par_value=250),
}

"""The default data model for GBCE"""
default_model = GBCEModel(stock_entries=default_stock_entries)
