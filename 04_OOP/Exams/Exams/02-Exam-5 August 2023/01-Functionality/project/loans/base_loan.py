from abc import ABC, abstractmethod


class BaseLoan(ABC):
    LOAN_TYPE = ""

    def __init__(self, interest_rate: float, amount: float):
        self.interest_rate = interest_rate
        self.amount = amount

    @abstractmethod
    def increase_interest_rate(self):
        ...
