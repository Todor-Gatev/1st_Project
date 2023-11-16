from abc import ABC, abstractmethod


class Astronaut(ABC):
    def __init__(self, name: str, oxygen: int):
        self.name = name
        self.oxygen = oxygen
        self.backpack = []

    # region getters and setters
    @property
    @abstractmethod
    def breathe(self):
        return 10

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not value.strip():
            raise ValueError("Astronaut name cannot be empty string or whitespace!")

        self.__name = value

    @property
    def oxygen(self):
        return self.__oxygen

    @oxygen.setter
    def oxygen(self, value):
        if value < 0:
            value = 0

        self.__oxygen = value
    # endregion

    def increase_oxygen(self, amount: int):
        self.oxygen += amount

    def get_info(self):
        items = ", ".join(self.backpack) if self.backpack else "none"

        return (f"Name: {self.name}\n"
                f"Oxygen: {self.oxygen}\n"
                f"Backpack items: {items}")
