# from sys import path
# print(*path, sep="\n")


# region MRO - Method Resolution Order - mro() -> list ; __mro__ -> tuple
class A:
    def rk(self):
        print(" In class A")


class B:
    def rk(self):
        print(" In class B")


class C(A, B):
    def __init__(self):
        print("Constructor C")


print(C.mro())  # [<class '__main__.C'>, <class '__main__.A'>, <class '__main__.B'>, <class 'object'>]
print(C.__mro__)  # (<class '__main__.C'>, <class '__main__.A'>, <class '__main__.B'>, <class 'object'>)
# endregion

# region Mixins, class NextIdMixin:, class RadioMixin:
# class NextIdMixin:
#     id = 0
#
#     @classmethod
#     def get_next_id(cls):
#         cls.id += 1
#
#         return cls.id
# endregion

# region super
# class Person(object):
#     def __init__(self, name):
#         self.name = name
#         self.__age = 5
#
#
# class Employee(Person):
#     def __init__(self, name, e_id):
#         super().__init__(name)
#         self.e_id = e_id
#
#
# e = Employee("Test", 123)
# print(e.name)
# endregion
