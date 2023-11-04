from typing import List

from project.animals.animal import Mammal
from project.food import Meat, Vegetable, Fruit


class Mouse(Mammal):

    def make_sound(self) -> str:
        return "Squeak"

    @property
    def weight_gain(self) -> float:
        return 0.10

    @property
    def food_can_eat(self) -> List:
        return [Vegetable, Fruit]


class Dog(Mammal):

    def make_sound(self) -> str:
        return "Woof!"

    @property
    def weight_gain(self) -> float:
        return 0.40

    @property
    def food_can_eat(self) -> List:
        return [Meat]


class Cat(Mammal):

    def make_sound(self) -> str:
        return "Meow"

    @property
    def weight_gain(self) -> float:
        return 0.30

    @property
    def food_can_eat(self) -> List:
        return [Vegetable, Meat]


class Tiger(Mammal):

    def make_sound(self) -> str:
        return "ROAR!!!"

    @property
    def weight_gain(self) -> float:
        return 1.00

    @property
    def food_can_eat(self) -> List:
        return [Meat]
