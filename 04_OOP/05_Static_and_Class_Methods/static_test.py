# class Pizza:
#     def __init__(self, ingredients):
#         self.ingredients = ingredients
#
#     @classmethod
#     def pepperoni(cls):
#         return cls(["tomato sauce", "parmesan", "pepperoni"])
#
#
# first_pizza = Pizza.pepperoni()
# print(first_pizza.ingredients)  # ['tomato sauce', 'parmesan', 'pepperoni']


# x = [[]] * 3  # [[], [], []]
# x[1].append(5)  # [[5], [5], [5]] !!!
# y = [[] for _ in range(3)]  # [[], [], []]
# y[1].append(5)  # [[], [5], []]
# y[1].append(5)  # [[], [5], []]
# print(y)

a = 4 / 2
print(a)
a = 5 // 2
print(a)
print(type(a))
