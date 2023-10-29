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

    def add_animal(self, animal, price) -> str:
        if len(self.animals) < self.__animal_capacity and self.__budget >= price:
            self.__budget -= price
            self.animals.append(animal)

            return f"{animal.name} the {animal.__class__.__name__} added to the zoo"
        elif len(self.animals) >= self.__animal_capacity:
            return "Not enough space for animal"
        else:
            return "Not enough budget"

    def hire_worker(self, worker) -> str:
        if len(self.workers) < self.__worker_capacity:
            self.workers.append(worker)

            return f"{worker.name} the {worker.__class__.__name__} hired successfully"

        return "Not enough space for worker"

    def fire_worker(self, worker_name: str) -> str:
        for w in self.workers:
            if w.name == worker_name:
                self.workers.remove(w)

                return f"{worker_name} fired successfully"

        return f"There is no {worker_name} in the zoo"

    def pay_workers(self) -> str:
        needed_amount = sum(w.salary for w in self.workers)

        if self.__budget < needed_amount:
            return "You have no budget to pay your workers. They are unhappy"

        self.__budget -= needed_amount

        return f"You payed your workers. They are happy. Budget left: {self.__budget}"

    def tend_animals(self) -> str:
        needed_amount = sum(a.money_for_care for a in self.animals)

        if self.__budget < needed_amount:
            return "You have no budget to tend the animals. They are unhappy."

        self.__budget -= needed_amount

        return f"You tended all the animals. They are happy. Budget left: {self.__budget}"

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self) -> str:
        info = {"Lion": [], "Tiger": [], "Cheetah": []}
        [info[a.__class__.__name__].append(str(a)) for a in self.animals]
        result = [
            f"You have {len(self.animals)} animals",
            f"----- {len(info['Lion'])} Lions:",
            *info["Lion"],
            f"----- {len(info['Tiger'])} Tigers:",
            *info["Tiger"],
            f"----- {len(info['Cheetah'])} Cheetahs:",
            *info["Cheetah"]
        ]

        return "\n".join(result)

    def workers_status(self):
        info = {"Keeper": [], "Caretaker": [], "Vet": []}
        [info[w.__class__.__name__].append(str(w)) for w in self.workers]
        result = [
            f"You have {len(self.workers)} workers",
            f"----- {len(info['Keeper'])} Keepers:",
            *info["Keeper"],
            f"----- {len(info['Caretaker'])} Caretakers:",
            *info["Caretaker"],
            f"----- {len(info['Vet'])} Vets:",
            *info["Vet"]
        ]

        return "\n".join(result)

