class Person:
    def __init__(self, name: str, age: int):
        self.__name = name
        self.__age = age

    @property
    def name(self):
        return self.__name

    def get_name(self):  # 32
        return self.__name

    def get_age(self):
        return self.__age


person = Person("George", 32)
print(person.name)
# print(person.get_name())  # George
print(person.get_age())  # 32
person.age = 37  # person.age is variable type(int) in that case
print(person.get_age())  # 32
print(person.age)  # <class 'int'>
print(type(person.age))  # 37 - person.age is variable in that case
# print(person.age())  # TypeError: 'int' object is not callable
