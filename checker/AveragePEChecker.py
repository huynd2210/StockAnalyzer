from checker.Checker import Checker
from entity.TickerInformation import TickerInformation

"""
Check if ticker PE is greater than the average PE of the market (e.g S&P 500)
"""
class AveragePEChecker(Checker):
    name = "Average PE Checker"
    def __init__(self, **kwargs):
        self.kwargs = kwargs
    def isTickerPassed(self, ticker: TickerInformation, **kwargs):
        kwargs = {**self.kwargs, **kwargs}
        defaultAveragePE = 30
        averagePE = kwargs.get("averagePE") or defaultAveragePE
        print(f'Average PE: {averagePE}')
        print(f'Ticker PE: {ticker.trailingPE}')
        return ticker.trailingPE > averagePE
