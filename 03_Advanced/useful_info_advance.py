from functools import reduce
map_functions = {
    '*': lambda x: reduce(lambda a, b: a * b, x),
    '/': lambda x: reduce(lambda a, b: a / b, x),
    '+': lambda x: reduce(lambda a, b: a + b, x),
    '-': lambda x: reduce(lambda a, b: a - b, x),
}  # 02_expression_evaluator_a.py  in  03_Stacks_Queues_Tuples_and_Sets_Exercise in advance

directions = {
    "U": (-1, 0),
    "D": (1, 0),
    "L": (0, -1),
    "R": (0, 1),
}
# p_row_new, p_col_new = p_row + directions[move][0], p_col + directions[move][1]

# map_functions = {
#     "Add First": lambda x: set_1.update(x),
#     "Add Second": lambda x: set_2.update(x),
#     "Remove First": lambda x: set_1.difference_update(x),
#     "Remove Second": lambda x: set_2.difference_update(x),
#     "Check Subset": lambda x: print(check_subset)
# }
# if map_functions.get(action):
#     map_functions[action](nums)
# else:
#     print("KeyError")
# try:
#     map_functions[action](nums)
# except KeyError:
#     pass
#     # print("KeyError")

# isinstance(length, int)
# bottles = list(map(int, input().split()))
# test = [1, 2, 3, 1, 7, 4, 1]
# indexes = [idx for idx, el in enumerate(test) if el == 1]
# indexes = [idx if el == 1 else print(el) for idx, el in enumerate(test)]

# import time
# from datetime import datetime, timedelta
# from collections import deque
# x_time = "8:00:00"
# line_time = datetime.strptime(x_time, "%H:%M:%S")
# start_time = time.time()
# diff = time.time() - start_time
# print(diff)
# 07_robotics in 01_Lists_as_Stacks_and_Queues in advance
