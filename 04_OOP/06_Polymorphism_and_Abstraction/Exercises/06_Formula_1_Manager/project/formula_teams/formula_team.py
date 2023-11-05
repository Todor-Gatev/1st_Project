from abc import ABC, abstractmethod
from typing import Dict


class FormulaTeam(ABC):
    def __init__(self, budget: int):
        self.budget = budget

    @property
    def budget(self):
        return self.__budget

    @budget.setter
    def budget(self, value):
        if value < 1_000_000:
            raise ValueError("F1 is an expensive sport, find more sponsors!")

        self.__budget = value

    @property
    @abstractmethod
    def expenses(self) -> int:
        ...

    @property
    @abstractmethod
    def sponsors(self) -> Dict[str, Dict[int, int]]:  # {sponsor: {position: reward}}
        ...

    def calculate_revenue_after_race(self, race_pos: int):
        revenue = - self.expenses

        for sponsor in self.sponsors:
            for position in self.sponsors[sponsor]:
                if race_pos <= position:
                    revenue += self.sponsors[sponsor][position]
                    break

        self.budget += revenue

        return f"The revenue after the race is {revenue}$. Current budget {self.budget}$"
