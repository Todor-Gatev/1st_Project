# from sys import path
#
# print(*path, sep="\n")


# from abc import ABC, abstractmethod
#
# class Base(ABC):
#     def __init__(self, ):
#
#     # region getters and setters
#
#     # endregion
#
#     @abstractmethod
#     def asd(self):
#         ...


# region getters and setters

# endregion


# region supporting methods
# def __get_

# endregion


# player = next(filter(lambda x: x.name == player_name, self.players), None)
# result2 = next(filter(lambda x: x == 7, my_list), "Not in list")

# VEHICLE_TYPES = {"PassengerCar": PassengerCar, "CargoVan": CargoVan}

# @property
# @abstractmethod
# def sponsors(self) -> Dict[str, Dict[int, int]]:  # {sponsor: {position: reward}}
#     ...

class A:

    # region supporting staff
    @staticmethod
    def find_object(collection: list, attribute: str, value: str):
        for obj in collection:
            if str(getattr(obj, attribute)) == value:
                return obj

    @staticmethod
    def get_objects(collection: list, attribute: str, value: str):
        return [obj for obj in collection if str(getattr(obj, attribute)) == value]
    # endregion


a = A()
print(type(a) == A)

# from unittest import TestCase, main
#
#
# class Test(TestCase):
#     def setUp(self) -> None:
#         self.
#
#     # def test_default_class_attributes_are_correct(self):
#     #     self.assertEqual(1.25, Vehicle.DEFAULT_FUEL_CONSUMPTION)
#     #
#     # def test_correct_initialization(self):
#     #     self.assertEqual()
#
#
# if __name__ == "__main__":
#     main()
