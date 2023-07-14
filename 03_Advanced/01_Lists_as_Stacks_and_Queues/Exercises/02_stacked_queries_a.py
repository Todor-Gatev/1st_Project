from collections import deque

stack = deque()

map_functions = {
    1: lambda x: stack.append(x[1]),
    2: lambda x: stack.pop() if stack else None,
    3: lambda x: print(max(stack)) if stack else None,
    4: lambda x: print(min(stack)) if stack else None,
}

# print(type(map_functions))

for _ in range(int(input())):
    command = [int(x) for x in input().split()]
    map_functions[command[0]](command)

# stack.reverse()
# # print(type(stack))
# print(*stack, sep=', ')
for _ in range(len(stack)):
    if len(stack) > 1:
        print(stack.pop(), end=', ')
    else:
        print(stack[0])
