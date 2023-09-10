from typing import List

from project.animal import Animal
# from project.caretaker import Caretaker
# from project.cheetah import Cheetah
# from project.keeper import Keeper
# from project.lion import Lion
# from project.tiger import Tiger
# from project.vet import Vet
from project.worker import Worker


class Zoo:
    def __init__(self, name: str, budget: int, animal_capacity: int, workers_capacity: int):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        # self.animals: List[Lion, Tiger, Cheetah] = []
        self.animals: List[Animal] = []
        # self.workers: List[Keeper, Caretaker, Vet] = []
        self.workers: List[Worker] = []

    def add_animal(self, animal: Animal, price: int) -> str:
        if self.__budget < price:
            return "Not enough budget"

        if self.__animal_capacity == len(self.animals):
            return "Not enough space for animal"

        self.__budget -= price
        self.animals.append(animal)

        return f"{animal.name} the {animal.__class__.__name__} added to the zoo"

    def hire_worker(self, worker: Worker) -> str:
        if self.__workers_capacity == len(self.workers):
            return "Not enough space for worker"

        self.workers.append(worker)

        return f"{worker.name} the {worker.__class__.__name__} hired successfully"

    def fire_worker(self, worker_name: str) -> str:
        try:
            w = next(filter(lambda x: x.name == worker_name, self.workers))
        except StopIteration:
            return f"There is no {worker_name} in the zoo"

        self.workers.remove(w)

        return f"{worker_name} fired successfully"
        #
        # for w in self.workers:
        #     if w.name == worker_name:
        #         self.workers.remove(w)
        #
        #         return f"{worker_name} fired successfully"
        # return "There is no {worker_name} in the zoo"

    def pay_workers(self) -> str:
        salaries = sum(w.salary for w in self.workers)

        # for w in self.workers:
        #     salaries += w.salary

        if self.__budget < salaries:
            return "You have no budget to pay your workers. They are unhappy"

        self.__budget -= salaries

        return f"You payed your workers. They are happy. Budget left: {self.__budget}"

    def tend_animals(self) -> str:
        total_money_for_care = 0

        for a in self.animals:
            total_money_for_care += a.money_for_care

        if self.__budget < total_money_for_care:
            return "You have no budget to tend the animals. They are unhappy."

        self.__budget -= total_money_for_care

        return f"You tended all the animals. They are happy. Budget left: {self.__budget}"

    def profit(self, amount: int) -> None:
        self.__budget += amount

    def animals_status(self) -> str:
        # lions = list(filter(lambda a: a.__class__.__name__ == "Lion", self.animals))
        # tiger = list(filter(lambda a: a.__class__.__name__ == "Tiger", self.animals))
        # cheetah = list(filter(lambda a: a.__class__.__name__ == "Cheetah", self.animals))

        # lions = []
        # tigers = []
        # cheetahs = []
        #
        # for a in self.animals:
        #     if a.__class__.__name__ == "Lion":
        #         lions.append(str(a))
        #     elif a.__class__.__name__ == "Tiger":
        #         tigers.append(str(a))
        #     elif a.__class__.__name__ == "Cheetah":
        #         cheetahs.append(str(a))
        info = {"Lion": [], "Tiger": [], "Cheetah": []}
        [info[a.__class__.__name__].append(str(a)) for a in self.animals]

        result = [
            f"You have {len(self.animals)} animals",
            f"----- {len(info['Lion'])} Lions:",
            *info["Lion"],
            f"----- {len(info['Tiger'])} Tigers:",
            *info["Tiger"],
            f"----- {len(info['Cheetah'])} Cheetahs:"
        ]
        # result.extend(lions)
        # result.append(f"----- {len(tigers)} Tigers:")
        # result.extend(tigers)
        # result.append(f"----- {len(cheetahs)} Cheetahs:")
        # result.extend(cheetahs)

        return "\n".join(result)

    def workers_status(self):
        info = {"Keeper": [], "Caretaker": [], "Vet": []}
        [info[w.__class__.__name__].append(str(w)) for w in self.workers]

        result = [f"You have {len(self.workers)} workers",
                  f"----- {len(info['Keeper'])} Keepers:",
                  *info["Keeper"],
                  f"----- {len(info['Caretaker'])} Caretakers:",
                  *info["Caretaker"],
                  f"----- {len(info['Vet'])} Vets:",
                  *info['Vet']
                  ]
        # result.extend(info["Keeper"])
        # result.append(f"----- {len(info['Caretaker'])} Caretakers:")
        # result.extend(info["Caretaker"])
        # result.append(f"----- {len(info['Vet'])} Vets:")
        # result.extend(info['Vet'])

        return "\n".join(result)

