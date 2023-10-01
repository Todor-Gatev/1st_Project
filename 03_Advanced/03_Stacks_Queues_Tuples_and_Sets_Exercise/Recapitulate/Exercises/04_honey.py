from collections import deque

working_bees = deque(map(int, input().split()))
nectar_list = [int(x) for x in input().split()]
symbols = deque(input().split())

honey = 0
map_function = {
    '+': lambda x, y: x + y,
    '-': lambda x, y: x - y,
    '/': lambda x, y: x if y == 0 else x / y,
    '*': lambda x, y: x * y,
}

while working_bees and nectar_list:
    nectar = nectar_list.pop()

    if nectar >= working_bees[0]:
        honey += abs(map_function[symbols.popleft()](working_bees.popleft(), nectar))

print(f"Total honey made: {honey}")

if working_bees:
    print(f"Bees left: {', '.join(str(x) for x in working_bees)}")

if nectar_list:
    print(f"Nectar left: {', '.join(str(x) for x in nectar_list)}")
