from typing import List

from project.dvd import Dvd


class Customer:
    def __init__(self, name: str, age: int, id_num: int):
        self.name = name
        self.age = age
        self.id = id_num
        self.rented_dvds: List[Dvd] = []

    def __repr__(self):
        return (f"{self.id}: {self.name} of age {self.age} has {len(self.rented_dvds)} rented DVD's"
                f" ({', '.join(d.name for d in self.rented_dvds)})")
