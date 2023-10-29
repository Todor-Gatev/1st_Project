class Person:
    def __init__(self, name: str, age: int):
        self.__name = name
        self.__age = age

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age


person = Person("George", 32)
print(person.get_name())
print(person.get_age())  # 32
person.age = 37  # person.age is variable in that case
print(person.get_age())  # 32
print(person.age)  # <class 'int'>
print(type(person.age))  # 37 - person.age is variable in that case
# print(person.age())  # TypeError: 'int' object is not callable


# class Person:
#     def __init__(self, name: str, age: int):
#         self.__name = name
#         self.__age = age  # _Person__age
#
#
# p = Person("Tom", 23)
#
# print(p.__age)  # AttributeError: 'Person' object has no attribute '__age'
# print(p._Person__age)  # 23
#
# p.__age = 47  # creates different instance variable than the one in "def __init__" =>  _Person__age
# print(p.__age)  # 47
# print(p._Person__age)  # 23

# class Person:
#     def __init__(self, age=0):
#         self.age = age
#
#     @property
#     def age(self):
#         return
#
#     @age.setter
#     def age(self, value):
#         if value < 18:
#             self.__age = 18
#         else:
#             self.__age = value
#         pass

    # @property
    # def age(self):
    #     return self.__age
    #
    # @age.setter
    # def age(self, age):
    #     if age < 18:
    #         self.__age = 18
    #     else:
    #         self.__age = age


# p = Person(12)
# print(p.age)
# p._Person__age = 11
# print(p.age)
# b = Person(14)
# print(b.age)


# class Person:
#     def __init__(self, age=0):
#         self.age = age
#
#
# person = Person(12)
# print(getattr(person, "age"))  # 12
# # print(getattr(person, "name"))  # AttributeError: 'Person' object has no attribute 'name'
# print(getattr(person, "name", "asd"))  # asd (if no such attr return "asd")
# print(getattr(person, "age", "asd"))  # 12

# class Person:
#     def __init__(self, age=0):
#         self.age = age
#
#     def __getattr__(self, item):
#         return "not .... blabla"
#
    # """__getattribute__ gets called “first”(the highest priority),
    #  whether or not there's the attribute.
    #   __getattr__ gets called “last”(the lowest priority),
    #    if Python cannot find the attribute"""

#
# person = Person(12)
# print(person.name)  # "not .... blabla"


# class Count:
#
#     def __init__(self, my_min, my_max):
#         self.my_min = my_min
#         self.my_max = my_max
#         self.current = None
#         self.test9 = None
#
#     def __getattribute__(self, item):
#         if item.startswith('curr') or item.endswith("9"):
#             raise AttributeError
#         return object.__getattribute__(self, item)
#         # or you can use ---return super().__getattribute__(item)


# obj1 = Count(1, 10)
# print(obj1.my_min)
# print(obj1.my_max)
# print(obj1.current)
# obj2 = Count(2, "19")
# print(obj2.my_max)
# print(obj2.test9)

# class Person:
#     def __init__(self, name):
#         self.name = name
#
#
# person = Person('Peter')
# print(setattr(person, 'name', 'George'))  # None
# print(person.name)                        # George
# print(setattr(person, 'age', 21))         # None
# print(person.age)                         # 21

# class Person:
#     TEST_ATTR = "test_attr"
#
#     def __init__(self, name: str, set_id):
#         self.name = name
#         self.id = set_id
#
#
# p1 = Person('Peter', 112)
# p1.name = "George"
# print(p1.name)                        # George
# p1.age = 7
# print(p1.age)                         # 7
# p2 = Person("Tom", 34)
# p3 = Person("Tim", 37)
# delattr(p1, "name")  # just for p1 instance
# # print(p1.name)  # AttributeError: 'Person' object has no attribute 'id'
# print(p2.name)  # Tom
# print(Person.TEST_ATTR)
# delattr(Person, "TEST_ATTR")  # None
# # print(Person.TEST_ATTR)  # AttributeError: type object 'Person' has no attribute 'TEST_ATTR'
#
# try:
#     delattr(Person, "name")  # type object 'Person' has no attribute 'name'
# except AttributeError:
#     print("type object 'Person' has no attribute 'name'")
#
# print(p2.name)
# print(p3.name)
#
#
