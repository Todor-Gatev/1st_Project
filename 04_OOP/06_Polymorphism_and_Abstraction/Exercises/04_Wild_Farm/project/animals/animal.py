from abc import ABC, abstractmethod
from typing import List

from project.food import Food


class Animal(ABC):
    def __init__(self, name: str, weight: float):
        self.name = name
        self.weight = weight
        self.food_eaten = 0

    @abstractmethod
    def make_sound(self) -> str:
        ...

    @property
    @abstractmethod
    def weight_gain(self) -> float:
        ...

    @property
    @abstractmethod
    def food_can_eat(self) -> List[Food]:
        ...

    def feed(self, food: Food) -> (str, None):
        if type(food) not in self.food_can_eat:
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"

        self.weight += self.weight_gain * food.quantity
        self.food_eaten += food.quantity


class Bird(Animal, ABC):
    def __init__(self, name: str, weight: float, wing_size: float):
        Animal.__init__(self, name, weight)
        self.wing_size = wing_size

    def __repr__(self):
        return f"{self.__class__.__name__} [{self.name}, {self.wing_size}, {self.weight}, {self.food_eaten}]"


class Mammal(Animal, ABC):
    def __init__(self, name: str, weight: float, living_region: str):
        Animal.__init__(self, name, weight)
        self.living_region = living_region

    def __repr__(self):
        return f"{self.__class__.__name__} [{self.name}, {self.weight}, {self.living_region}, {self.food_eaten}]"

