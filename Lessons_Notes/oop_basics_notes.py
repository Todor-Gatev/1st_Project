from typing import List, Callable

# from collections.abc import Callable, Awaitable

# pascal case
idk_list: list[int, str, float] = [5, "hi", 4.7]


class MyClass:
    """This is MyClass."""

    def example(self):
        """This is the example module of MyClass."""


print(MyClass.__doc__) # This is MyClass.
print(MyClass.example.__doc__)
# This is the example module of MyClass.


class Shop:
    def __init__(self, name, items: List[str]):
        self.name = name
        self.items = items

    def get_items_count(self):
        # def get_items_count(self) -> Callable:
        return len(self.items)


class Hero:
    def __init__(self, name: str, health: int):
        self.name = name
        self.health = health

    def defend(self, damage: int) -> None or str:
        self.health -= damage

        if self.health <= 0:
            self.health = 0
            return f"{self.name} was defeated"

    def heal(self, amount: int) -> None:
        self.health += amount


b = 7


def ft(var_1):
    b = 9
    print(b)


ft(b)  # 9
print(b)  # 7

# def sum(lst1) -> float:
#     return lst1
#
#
# a = sum([1, 2, 3])
# print(a)


# def not_recursion():
#     def not_recursion():
#         def not_recursion():
#             print(3)
#
#         print(2)
#         not_recursion()
#
#     print(1)
#     not_recursion()
#
# not_recursion()
