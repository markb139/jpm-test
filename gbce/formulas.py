from operator import mul
import math

"""Financial formulas as given in requirements"""

def calc_common_dividend_yield(last_dividend, price):
    """Calculate dividend yield for common stocks.

    :param float last_dividend: the last dividend
    :param float price: current price

    :return: yield
    """
    return last_dividend/price


def calc_preferred_dividend_yield(dividend, par_value, price):
    """Calculate dividend yield for preferred stocks.

    :param float last_dividend: the last dividend
    :param float price: current price

    :return: yield
    """
    return dividend*par_value/price


def calc_pe_ratio(dividend, price):
    """Calculate P/E ratio.

    :param float dividend: the dividend
    :param float price: current price

    :return: p/e ratio
    """
    return price/dividend


def calc_geometric_mean(prices):
    """Calculate geometric mean.

    :param list prices

    :return: mean
    """
    if prices:
        f = reduce(mul, prices, 1.0)
        return math.pow(f, 1.0/len(prices))
    else:
        return 1.0


def calc_volume_weighted_stock_price(trades):
    """Calculate volume weighted stock price.

    :param list proces: list of (price, quantity) tuples

    :return: price
    """

    if trades:
        prices, quantity = zip(*trades)
        return sum(map(mul, prices, quantity))/sum(quantity)
    else:
        return 0.0
