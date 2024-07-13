from checker.Checker import Checker
from entity.TickerInformation import TickerInformation

"""
Check if ticker PEG < 1.0
"""
class PEGChecker(Checker):
    name = "PEG Checker"
    def __init__(self, **kwargs):
        self.kwargs = kwargs
    def isTickerPassed(self, ticker: TickerInformation, **kwargs):
        kwargs = {**self.kwargs, **kwargs}
        defaultAveragePE = 30
        averagePE = kwargs.get("averagePEG") or defaultAveragePE
        print(f'Average PE: {averagePE}')
        print(f'Ticker PE: {ticker.trailingPE}')
        return ticker.trailingPE > averagePE
