from collections import deque

working_bees = deque(map(int, input().split()))
nectar_list = list(map(int, input().split()))
symbols = deque(input().split())

total_honey = 0

map_functions = {
    '*': lambda x, y: x * y,
    '/': lambda x, y: x / y,
    '+': lambda x, y: x + y,
    '-': lambda x, y: y - x
}

while working_bees and nectar_list:
    nectar = nectar_list.pop()
    bee = working_bees.popleft()

    if nectar < bee:
        working_bees.appendleft(bee)
    elif nectar >= bee and nectar != 0:
        total_honey += map_functions[symbols.popleft()](bee, nectar)

print(f"Total honey made: {total_honey}")

if working_bees:
    print(f"Bees left: ", end='')
    print(*working_bees, sep=", ")
elif nectar_list:
    print(f"Nectar left: ", end='')
    print(*nectar_list, sep=", ")
