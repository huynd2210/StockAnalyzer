from typing import List

from checker.BenjaminGrahamChecker import BenjaminGrahamChecker
from checker.Checker import Checker
from entity.TickerInformation import TickerInformation
import yfinance as yf

from screener.AllPassScreener import AllPassScreener

def screenTicker(ticker: TickerInformation, checkers: List[Checker]) -> bool:
    allPassScreener = AllPassScreener()
    return allPassScreener.screenTicker(ticker, checkers)

#Test
if __name__ == '__main__':
    ticker = yf.Ticker("TSM")
    tickerInfoEntity = TickerInformation(ticker.info)
    isPassed = screenTicker(tickerInfoEntity, [BenjaminGrahamChecker(isDebug=True)])
    print("---------------------------")
    print(isPassed)