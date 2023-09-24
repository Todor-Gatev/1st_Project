# from sys import path
# print(*path, sep="\n")

# a, *info = input().split()
#
# if isinstance(int(a), int):
#     print(a)

orders = list("abcdf")
print("Orders left:", *orders, "end", '.')
