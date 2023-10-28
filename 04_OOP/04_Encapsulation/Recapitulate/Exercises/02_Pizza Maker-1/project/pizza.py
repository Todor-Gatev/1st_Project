from typing import Dict

from project.dough import Dough
from project.topping import Topping


class Pizza:
    def __init__(self, name: str, dough: Dough, max_number_of_toppings: int):
        self.name = name
        self.dough = dough
        self.max_number_of_toppings = max_number_of_toppings
        self.toppings: Dict[str: float] = {}  # {topping_type: topping_weight}

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value:
            self.__name = value
        else:
            raise ValueError("The name cannot be an empty string")

    @property
    def dough(self):
        return self.__dough

    @dough.setter
    def dough(self, value):
        if value:
            self.__dough = value
        else:
            raise ValueError("You should add dough to the pizza")

    @property
    def max_number_of_toppings(self):
        return self.__max_number_of_toppings

    @max_number_of_toppings.setter
    def max_number_of_toppings(self, value):
        if value > 0:
            self.__max_number_of_toppings = value
        else:
            raise ValueError("The maximum number of toppings cannot be less or equal to zero")

    def add_topping(self, topping: Topping):
        if len(self.toppings) < self.max_number_of_toppings:
            self.toppings[topping] = self.toppings.get(topping, 0) + topping.weight
        else:
            raise ValueError("Not enough space for another topping")

    def calculate_total_weight(self) -> float:
        return sum(self.toppings.values()) + self.dough.weight
