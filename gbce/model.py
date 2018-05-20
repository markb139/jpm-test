from datetime import datetime, timedelta

from gbce.datastore import DataStore

from .formulas import calc_volume_weighted_stock_price, calc_geometric_mean
from .stocks import CommonStock, PreferredStock


class GBCEModel(object):
    def __init__(self, stocks):
        self.entries = stocks
        self.store = DataStore()

    @property
    def count(self):
        return self.store.count

    def dividend_yield(self, symbol, price):
        return self.entries[symbol].dividend_yield(price=price)

    def pe_ratio(self, symbol, price):
        return self.entries[symbol].pe_ratio(price=price)

    def volume_weighted_price(self, symbol):
        timestamp = datetime.utcnow() - timedelta(minutes=5)
        trades = map(lambda e: (e.price, e.quantity), self.store.find(symbol=symbol,timestamp=timestamp))
        return calc_volume_weighted_stock_price(trades=trades)

    def all_share_index(self):
        timestamp = datetime.utcnow() - timedelta(minutes=5)
        prices = []
        for symbol in self.entries.keys():
            trades = map(lambda e: (e.price, e.quantity), self.store.find(symbol=symbol,timestamp=timestamp))
            if trades:
                prices.append(calc_volume_weighted_stock_price(trades=trades))
        return calc_geometric_mean(prices)


    def record(self, trade):
        self.store.append(trade)

stocks = {
    'TEA': CommonStock(last_dividend=0.0, par_value=100),
    'POP': CommonStock(last_dividend=8.0, par_value=100),
    'ALE': CommonStock(last_dividend=23.0, par_value=60),
    'GIN': PreferredStock(last_dividend=8.0, fixed_dividend=0.02, par_value=100),
    'JOE': CommonStock(last_dividend=13.0, par_value=250),
}
default_model = GBCEModel(stocks=stocks)