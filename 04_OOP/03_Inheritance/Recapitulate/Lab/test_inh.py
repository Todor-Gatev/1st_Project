# class Vehicle:
#     DEFAULT_FUEL_CONSUMPTION: float = 1.25
#
#     def __init__(self, fuel: float, horse_power: int):
#         self.fuel = fuel
#         self.horse_power = horse_power
#         self.fuel_consumption = self.DEFAULT_FUEL_CONSUMPTION
#         # self.fuel_consumption = Vehicle.DEFAULT_FUEL_CONSUMPTION
#
#
# # is_long_enough = len(value) > 7
# # is_upper_char = [x for x in value if x.isupper()]
# # is_digit_in_password = [x for x in value if x.isdigit()]
# c = Vehicle(3, 7)
# print(c.__repr__())
# print(c.__class__.__name__)
#
# a = {'a': 1, 'b': 2, 'c': 's'}
# print(len(a))


from abc import ABC, abstractmethod


class Animal(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def sound(self):
        raise NotImplementedError("Subclass must implement")


#
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
animal = Animal("Willy")  # TypeError: Can't instantiate abstract class Animal with abstract method sound
# animal.sound()
