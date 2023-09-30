from collections import deque
from functools import reduce

data = deque(input().split())
temp_list = []

map_function = {
    '+': lambda x: reduce(lambda a, b: a + b, x),
    '-': lambda x: reduce(lambda a, b: a - b, x),
    '/': lambda x: int(reduce(lambda a, b: a / b, x)),
    # '/': lambda x: reduce(lambda a, b: a + b if a == 0 or b == 0 else a / b, x),
    '*': lambda x: reduce(lambda a, b: a * b, x),
}

for el in data:
    if el in map_function:
        res = map_function[el](temp_list)
        temp_list.clear()
        temp_list.append(res)
    else:
        temp_list.append(int(el))

print(temp_list[0])
