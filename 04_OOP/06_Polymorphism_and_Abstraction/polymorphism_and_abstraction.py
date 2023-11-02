# class Person:
#     def say_hello():
#         return "Hi!"
#
#     def say_hello():
#         return "Hello"
#
#
# print(Person.say_hello())  # Hello

# region Polymorphism vs Duck typing

# region Polymorphism needs inheritance for overriding method of superclass
class Robot:
    def __init__(self, name):
        self.name = name

    @staticmethod
    def sensors_amount():
        return 1


class MedicalRobot(Robot):
    @staticmethod
    def sensors_amount():
        return 6


class ChefRobot(Robot):
    @staticmethod
    def sensors_amount():
        return 4


def number_of_robot_sensors(robot):   # object must be Robot type - Polymorphism
    try:
        print(robot.sensors_amount())
    except AttributeError:
        print("unknown robot")


basic_robot = Robot('Robo')
da_vinci = MedicalRobot('Da Vinci')
moley = ChefRobot('Moley')

number_of_robot_sensors(basic_robot)
number_of_robot_sensors(da_vinci)
number_of_robot_sensors(moley)


# endregion -

# region Duck Typing can create a method that calls the sound method,
# no matter what the object which makes the sound is

# def number_of_robot_sensors(robot):   # object must be Robot type - Polymorphism
def start_playing(obj):  # it can be any type of obj, but obj must have play method - duck typing
    return obj.play()


class Guitar:
    def play(self):
        return "Playing the guitar"


class Children:
    def play(self):
        return "Children are playing"


guitar = Guitar()
start_playing(guitar)
piano = Children()
start_playing(piano)


# next example
class Cat:
    def sound(self):
        print("Meow!")


class Train:
    def sound(self):
        print("Sound from wheels slipping!")


for any_type in Cat(), Train():
    any_type.sound()

# endregion

# endregion


# region Robots polymorphism

# class Robot:
#     _diodes_amount = "d1"
#
#     def __init__(self, name):
#         self.name = name
#
#     @classmethod
#     def diodes_amount(cls):
#         return cls._diodes_amount
#
#     @staticmethod
#     def sensors_amount():
#         return 1
#
#
# class MedicalRobot(Robot):
#     _diodes_amount = "d6"
#
#     @staticmethod
#     def sensors_amount():
#         return 6
#
#
# class ChefRobot(Robot):
#     _diodes_amount = "d4"
#
#     @staticmethod
#     def sensors_amount():
#         return 4
#
#
# class WarRobot(Robot):
#     _diodes_amount = "d12"
#
#     @staticmethod
#     def sensors_amount():
#         return 12
#
#
# def number_of_robot_sensors(robot):
#     try:
#         print(robot.sensors_amount())
#     except AttributeError:
#         print("unknown robot")
#
#
# def number_of_robot_diodes(robot):
#     try:
#         print(robot.diodes_amount())
#     except AttributeError:
#         print("unknown robot")
#
#
# class Person:
#     def __init__(self, name):
#         self.name = name
#
#
# basic_robot = Robot('Robo')
# da_vinci = MedicalRobot('Da Vinci')
# moley = ChefRobot('Moley')
# griffin = WarRobot('Griffin')
# p = Person("asd")
#
# number_of_robot_sensors(basic_robot)
# number_of_robot_sensors(da_vinci)
# number_of_robot_sensors(moley)
# number_of_robot_sensors(griffin)
# number_of_robot_sensors(p)
#
# number_of_robot_diodes(basic_robot)
# number_of_robot_diodes(da_vinci)
# number_of_robot_diodes(moley)
# number_of_robot_diodes(griffin)
# number_of_robot_diodes(p)
#
# print(isinstance(moley, Robot))

# endregion


# region Abstraction

# region from abc import ABC, abstractmethod
from abc import ABC, abstractmethod


class Animal(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def sound(self):
        # raise NotImplementedError("Subclass must implement")
        ...


class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)

    def sound(self):
        print("Bark!")


class Cat(Animal):
    def __init__(self, name):
        super().__init__(name)

    def sound(self):
        print("Meow!")


cat = Cat("Willy")
cat.sound()
dog = Dog("Willy")
dog.sound()


# animal = Animal("Willy")  # TypeError: Can't instantiate abstract class Animal with abstract method sound
# animal.sound()

# endregion


# region Abstraction could be achieved using exceptions, but it not a good practice
class Shape:
    def __init__(self):
        if type(self) is Shape:
            raise Exception('This is an abstract class')

    def area(self):
        raise Exception('This is an abstract class')

    def perimeter(self):
        raise Exception('This is an abstract class')
# endregion


# endregion
