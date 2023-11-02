class Person:
    min_age = 0
    max_age = 150

    def __init__(self, name, age):
        self.name = name
        self.age = age

    # region find object via attribute value
    @staticmethod
    def find_object(collection: list, attribute: str, value: str):
        for obj in collection:
            if str(getattr(obj, attribute)) == value:
                return obj

    # endregion

    @classmethod
    def __validate_age(cls, value):
        if value < cls.min_age or value > cls.max_age:
            raise ValueError(f'{value} must be between '
                             f'{cls.min_age} and {cls.max_age}')

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        self.__validate_age(value)
        self.__age = value


class Employee(Person):
    min_age = 16

    # __validate_age() takes the class attribute min_age of class Employee

    def __init__(self, name, age, salary):
        super().__init__(name, age)  # when checking the age of the Employee
        self.salary = salary


p = Person("asd", 12)  # no error for age


# e = Employee("test", 12, 34)  # ValueError: 12 must be between 16 and 150


class NextIdMixin:
    id = 0

    @classmethod
    def get_next_id(cls):
        cls.id += 1

        return cls.id
