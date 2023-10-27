from sys import path
print(*path, sep="\n")

# a, *info = input().split()

# if isinstance(int(a), int):
#     print(a)

# orders = list("abcdf")
# print("Orders left:", *orders, "end", '.')

# knight_attacks = len({(i + di, j + dj) for di, dj in positions if (i + di, j + dj) in knights})
# knight_attacks = len({(i + di, j + dj) for di, dj in positions}.intersection(knights))
# faster than the upper row due to intersection.
# intersection is faster than if !!!

# class Car:
#     def __init__(self, fuel: int):
#         self.fuel = fuel
#         self.__max_speed = 200
#
#     def drive(self):
#         print('driving max speed ' + str(self.__max_speed))
#
#     @property
#     def fuel(self):
#         return self.__fuel
#
#     @fuel.setter
#     def fuel(self, value):
#         if value < 100:
#             self.__fuel = value
#
#     def __get_fuel_and_speed(self):  # "private"  class method
#         return f"{self.fuel} - {self.__max_speed}"
#
#     def get_info(self):
#         return self.__get_fuel_and_speed()
#
#
# red_car = Car(47)
# # print(red_car.__max_speed) # AttributeError: 'Car' object has no attribute '__max_speed'
# # print(red_car._Car__max_speed)  # 200
# red_car.drive()  # driving max speed 200
# red_car.__max_speed = 10  # won't change because it is name mangled
# red_car.drive()  # driving max speed 200
# print(red_car.fuel)  # 47
# red_car.fuel = 120  # 47 because 120 > 100 - AttributeError if no @fuel.setter
# red_car.fuel = 83  # 83 - AttributeError if no @fuel.setter
# # print(red_car.__get_fuel_and_speed())  # AttributeError: 'Car' object has no attribute '__get_fuel_and_speed'
# print(red_car.get_info())  # 83 - 200

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_info(self):
        return f'{self.name} is {self.age} years old.'


class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    def get_id(self):
        return self.student_id


# Create an object of the superclass
person = Person("John", 25)
print(person.get_info())
# returns 'John is 25 years old.'

# Create an object of the subclass
student = Student("Leo", 20, 10035464)
print(student.get_info())
# returns 'Leo is 20 years old.'
print(student.get_id())
# returns 10035464
