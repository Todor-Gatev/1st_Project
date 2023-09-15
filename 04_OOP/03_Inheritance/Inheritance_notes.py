# from sys import path
# print(*path, sep="\n")


class Person(object):
    def __init__(self, name):
        self.name = name
        self.__age = 5


class Employee(Person):
    def __init__(self, name, e_id):
        super().__init__(name)
        self.e_id = e_id


e = Employee("Test", 123)
print(e.name)
