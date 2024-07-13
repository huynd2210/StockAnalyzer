from checker.Checker import Checker
from entity.TickerInformation import TickerInformation

"""
Check if the total debt is greater than the operating cashflow
"""

class DebtChecker(Checker):
    name = "Debt Coverage Checker"

    def __init__(self, **kwargs):
        self.kwargs = kwargs

    def isTickerPassed(self, ticker: TickerInformation, **kwargs):
        kwargs = {**self.kwargs, **kwargs}

        totalDebt = ticker.totalDebt
        operatingCashflow = ticker.operatingCashflow
        print(f'Total Debt: {totalDebt}')
        print(f'Operating Cashflow: {operatingCashflow}')
        return operatingCashflow >= totalDebt
