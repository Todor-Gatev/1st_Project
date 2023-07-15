from collections import deque
from functools import reduce

expression = deque(input().split())
nums = deque()

map_functions = {
    '*': lambda x: reduce(lambda a, b: a * b, x),
    '/': lambda x: reduce(lambda a, b: a / b, x),
    '+': lambda x: reduce(lambda a, b: a + b, x),
    '-': lambda x: reduce(lambda a, b: a - b, x),
}

while expression:
    el = expression.popleft()
    if el not in "*-+/":
        nums.append(int(el))
    else:
        num = int(map_functions[el](nums))
        nums.clear()
        nums.append(num)

print(nums.popleft())
