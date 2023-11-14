from typing import List

from project.animals.animal import Bird
from project.food import Food, Meat, Vegetable, Fruit, Seed


class Owl(Bird):

    def make_sound(self) -> str:
        return "Hoot Hoot"

    @property
    def weight_gain(self) -> float:
        return 0.25

    @property
    def food_can_eat(self) -> List:
        return [Meat]


class Hen(Bird):

    def make_sound(self) -> str:
        return "Cluck"

    @property
    def weight_gain(self) -> float:
        return 0.35

    @property
    def food_can_eat(self) -> List:
        return [Vegetable, Fruit, Meat, Seed]
