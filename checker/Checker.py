from abc import ABC, abstractmethod


class Checker(ABC):

    name = "N/A"
    @abstractmethod
    def isTickerPassed(self, ticker, **kwargs) -> bool:
        pass
