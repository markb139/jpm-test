from operator import mul
import math


def calc_common_dividend_yield(last_dividend, price):
    return last_dividend/price


def calc_preferred_dividend_yield(dividend, par_value, price):
    return dividend*par_value/price


def calc_pe_ratio(dividend, price):
    return price/dividend


def calc_geometric_mean(prices):
    if prices:
        f = reduce(mul, prices, 1.0)
        return math.pow(f, 1.0/len(prices))
    else:
        return 1.0


def calc_volume_weighted_stock_price(trades):
    if trades:
        prices, quantity = zip(*trades)
        return sum(map(mul, prices, quantity))/sum(quantity)
    else:
        return 0.0
