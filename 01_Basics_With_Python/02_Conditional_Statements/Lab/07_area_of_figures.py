from math import pi

# Read user input
type_of_the_figure = input()
# Logic
result = 0

if type_of_the_figure == "square":
    side = float(input())
    result = side ** 2
elif type_of_the_figure == "rectangle":
    first_side = float(input())
    second_side = float(input())
    result = first_side * second_side
elif type_of_the_figure == "circle":
    radius = float(input())
    result = pi * (radius ** 2)
elif type_of_the_figure == "triangle":
    side = float(input())
    height = float(input())
    result = side * height / 2

# Print Output
print(f"{result:.3f}")

# Read user input
#
# Logic
#
# Print Output
#
# from math import ceil, floor
# # import math
# x = 5.98
# print(floor(x))
# print(ceil(x))
# print(int(x))

# x = 4.5
# y = 5.5
# print(round(x))
# print(round(y))

# print(round(x, 2))
# print(f"{x:.2f}")
