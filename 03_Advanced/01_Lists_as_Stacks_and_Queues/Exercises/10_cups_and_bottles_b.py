from collections import deque


cups = deque(map(int, input().split()))
bottles = list(map(int, input().split()))

wasted_litters_of_water = 0

while cups and bottles:
    cup = cups[0]

    while bottles:
        bottle = bottles.pop()

        if bottle >= cup:
            wasted_litters_of_water += bottle - cup
            cups.popleft()
            break
        else:
            cup -= bottle

if cups:
    print("Cups: ", end='')
    print(*cups)
else:
    print("Bottles: ", end='')
    print(*bottles)

print(f"Wasted litters of water: {wasted_litters_of_water}")
