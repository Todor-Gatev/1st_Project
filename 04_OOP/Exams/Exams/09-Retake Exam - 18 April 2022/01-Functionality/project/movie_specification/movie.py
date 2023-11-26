from abc import ABC, abstractmethod


class Movie(ABC):
    def __init__(self, title: str, year: int, owner: object, age_restriction: int):
        self.title = title
        self.year = year
        self.owner = owner  # User
        self.age = age_restriction
        self.likes: int = 0

    # region getters and setters
    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, value):
        if not value:
            raise ValueError("The title cannot be empty string!")
        self.__title = value

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, value):
        if value < 1888:
            raise ValueError("Movies weren't made before 1888!")

        self.__year = value

    @property
    def owner(self):
        return self.__owner

    @owner.setter
    def owner(self, value):
        if value.__class__.__name__ is not "User":
            raise ValueError("The owner must be an object of type User!")

        self.__owner = value

    @property
    @abstractmethod
    def age_restriction(self):
        ...

    @age_restriction.setter
    def age_restriction(self, value):
        ...

    # endregion

    @abstractmethod
    def details(self):
        ...
