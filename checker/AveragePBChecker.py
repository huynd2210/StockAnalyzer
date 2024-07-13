from checker.Checker import Checker
from entity.TickerInformation import TickerInformation

"""
Check if ticker PB is greater than the average PE of the market (e.g S&P 500)
"""
class AveragePBChecker(Checker):
    name = "Average PB Checker"
    def __init__(self, **kwargs):
        self.kwargs = kwargs
    def isTickerPassed(self, ticker: TickerInformation, **kwargs):
        kwargs = {**self.kwargs, **kwargs}
        defaultAveragePB = 30
        averagePB = kwargs.get("averagePB") or defaultAveragePB
        print(f'Average PB: {averagePB}')
        print(f'Ticker PB: {ticker.priceToBook}')
        return ticker.priceToBook > averagePB
