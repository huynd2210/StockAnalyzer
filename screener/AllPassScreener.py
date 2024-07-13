from typing import List

from checker.Checker import Checker
from entity.TickerInformation import TickerInformation
from screener.Screener import Screener, printScreenerInformation

"""
A ticker is considered passed if all the checkers pass.
"""
class AllPassScreener(Screener):
    @printScreenerInformation
    def screenTicker(self, ticker: TickerInformation, checkers: List[Checker], **kwargs) -> bool:
        for checker in checkers:
            if not checker.isTickerPassed(ticker):
                return False
        return True
