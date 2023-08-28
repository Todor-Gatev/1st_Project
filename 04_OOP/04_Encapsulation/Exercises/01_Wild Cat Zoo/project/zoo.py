from typing import List

from project.caretaker import Caretaker
from project.cheetah import Cheetah
from project.keeper import Keeper
from project.lion import Lion
from project.tiger import Tiger
from project.vet import Vet


class Zoo:
    def __init__(self, name: str, budget: int, animal_capacity: int, worker_capacity: int):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__worker_capacity = worker_capacity
        self.animals: List[Lion, Tiger, Cheetah] = []
        self.workers: List[Keeper, Caretaker, Vet] = []

    # def add_animal(self, animal: (Lion, Tiger, Cheetah), price: int) -> str:
    #     if self.__animal_capacity and self.__budget >= price:
    #         return f"{name} the {type of animal (Lion/Tiger/Cheetah)} added to the zoo"
