from .formulas import calc_common_dividend_yield, calc_preferred_dividend_yield, calc_pe_ratio


class CommonStock(object):
    """Common stock class"""
    last_dividend = 0.0
    par_value = 0.0

    def __init__(self, last_dividend=0.0, par_value=0.0):
        self.last_dividend = last_dividend
        self.par_value = par_value

    def dividend_yield(self, price):
        return calc_common_dividend_yield(last_dividend=self.last_dividend, price=price)

    def pe_ratio(self, price):
        return calc_pe_ratio(dividend=self.last_dividend, price=price)


class PreferredStock(CommonStock):
    """Preferred stock class"""
    fixed_dividend = 0.0

    def __init__(self, fixed_dividend=0.0, **kwargs):
        super(PreferredStock, self).__init__(**kwargs)
        self.fixed_dividend = fixed_dividend

    def dividend_yield(self, price):
        return calc_preferred_dividend_yield(dividend=self.fixed_dividend, par_value=self.par_value, price=price)
