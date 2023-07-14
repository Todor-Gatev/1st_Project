from collections import deque

stack = deque()

for _ in range(int(input())):
    command = input().split()
    action = command[0]
    if action == '1':
        stack.append(int(command[1]))
    elif stack:
        if action == '2':
            stack.pop()
        elif action == '3':
            print(max(stack))
        elif action == '4':
            print(min(stack))

result = ""
while stack:
    result += str(stack.pop()) + ", "

print(result[:-2])
