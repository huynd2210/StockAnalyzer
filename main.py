from openbb import obb
from box import Box
import matplotlib.pyplot as plt
import yfinance as yf
import pprint

from entity.TickerInformation import TickerInformation


def getTickerInfo(ticker, wrapInBox=True):
    ticker = yf.Ticker(ticker)
    if wrapInBox:
        return Box(ticker.info)
    return ticker.info

def getDerivativeInfo(contract_name):
    # Replace this with the contract name you are interested in
    # Fetch data about the contract
    derivative = yf.Ticker(contract_name)

    # Print the information about the derivative
    derivative_info = derivative.info

    # Access specific details
    return derivative_info

# Main function
if __name__ == "__main__":


    # plot_stock_data(ticker, start_date, end_date)

    ticker = yf.Ticker("TSM")
    msftInfoEntity = TickerInformation(ticker.info)
    # get all stock info
    # pprint.pp(ticker.info)
    print("---------------------------")
    bs = ticker.balance_sheet
    # pprint.pp(bs)

    print(bs.loc['Cash And Cash Equivalents'].iloc[0])


    # print(bs["Cash Equivalents"])
    # for index, row in bs.iterrows():
    #     print(index)
    #     print("row: ", row)
    #     print("row keys: ", row.keys())
    #     print("---------------------------")


    # pprint.pp(getDerivativeInfo("MSFT240621C00110000"))

    # print(msftInfoEntity.industry)
