import inspect
from abc import ABC, abstractmethod
from typing import List

from checker.Checker import Checker
from entity.TickerInformation import TickerInformation


def printScreenerInformation(func):
    def wrapper(*args, **kwargs):
        checkers = args[2]

        signature = inspect.signature(func)
        bound_arguments = signature.bind(*args, **kwargs)
        bound_arguments.apply_defaults()

        if 'checkers' in bound_arguments.arguments:
            checkers = bound_arguments.arguments['checkers']

        print(f'Running checkers: {[checker.name for checker in checkers]}')
        return func(*args, **kwargs)
    return wrapper
class Screener(ABC):
    @abstractmethod
    def screenTicker(self, ticker: TickerInformation, checkers: List[Checker], **kwargs) -> bool:
        pass