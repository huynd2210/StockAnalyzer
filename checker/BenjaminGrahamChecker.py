from dataclasses import dataclass

from checker.Checker import Checker
from entity.TickerInformation import TickerInformation

class BenjaminGrahamChecker(Checker):

    name = "Benjamin Graham Revised Formula"
    def __init__(self, **kwargs):
        self.kwargs = kwargs

    def isTickerPassed(self, ticker: TickerInformation, **kwargs) -> bool:
        kwargs = {**self.kwargs, **kwargs}

        basePENoGrowth = kwargs.get("basePENoGrowth") or 8.5

        defaultAverageBondYield = 4.4
        defaultCurrentBondYield = 5.0

        averageBondYield = kwargs.get("averageBondYield") or defaultAverageBondYield
        earningGrowthRate = kwargs.get("earningGrowthRate") or ticker.earningsGrowth
        currentBondYield = kwargs.get("currentBondYield") or defaultCurrentBondYield

        formulaValue = ticker.trailingEps * (basePENoGrowth + (2 * (earningGrowthRate * 100))) * averageBondYield
        formulaValue = formulaValue / currentBondYield

        if kwargs.get("isDebug"):
            self._print_debug_logs(basePENoGrowth, earningGrowthRate, averageBondYield, currentBondYield, ticker.trailingEps)

        print(f'Benjamin Graham Value: {formulaValue}')

        currentTickerPrice = ticker.currentPrice
        print(f'Current Ticker Price: {currentTickerPrice}')
        return formulaValue > currentTickerPrice

    def _print_debug_logs(self, basePENoGrowth, earningGrowthRate, averageBondYield, currentBondYield, tickerTrailingEPS):
        print(f'basePENoGrowth: {basePENoGrowth}')
        print(f'earningGrowthRate: {earningGrowthRate}')
        print(f'averageBondYield: {averageBondYield}')
        print(f'currentBondYield: {currentBondYield}')
        print(f'tickerTrailingEPS: {tickerTrailingEPS}')
