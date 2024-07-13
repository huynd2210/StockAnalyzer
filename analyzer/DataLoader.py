import yfinance as yf
import pickle

import pandas as pd
from backtrader.feeds import YahooFinanceData
def retrieveData(tickerSymbol, periods=None):
    if periods is None:
        periods = ['10y', '5y', '2y', '1y', '6mo', '3mo']
    tickerData = yf.Ticker(tickerSymbol)

    for period in periods:
        try:
            tickerDf = tickerData.history(period=period)
            if not tickerDf.empty:
                return tickerDf
        except Exception as e:
            print(f"Failed to retrieve data for period {period}: {e}")

    print(f"Data not available for any of the specified periods for ticker {tickerSymbol}")
    return None

def saveFinanceData(data, filePath="financialData.pickle"):
    with open(filePath, 'wb') as f:
        pickle.dump(data, f)

def loadFinanceData(filePath="financialData.pickle"):
    with open(filePath, 'rb') as f:
        data = pickle.load(f)
    return data

def readTickerSymbols(filename):
    tickerSymbols = []
    with open(filename) as f:
        for line in f:
            tickerSymbols.append(line.split('\t')[0].strip())
    return tickerSymbols


if __name__ == '__main__':
    res = set()
    filename = "../NASDAQ.txt"
    nasdaq = readTickerSymbols(filename)

    filename2 = "../NYSE.txt"
    nyse = readTickerSymbols(filename2)

    for ticker in nasdaq:
        res.add(ticker)

    for ticker in nyse:
        res.add(ticker)
    print(res)

    financeData = {}

    for e in res:
        financeData[e] = retrieveData(e)


