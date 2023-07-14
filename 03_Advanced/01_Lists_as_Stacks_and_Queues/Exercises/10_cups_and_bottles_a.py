from collections import deque

cups = deque(int(x) for x in input().split())
bottles = list(map(int, input().split()))

wasted_litters_of_water = 0

while cups and bottles:
    bottle_litters = bottles.pop()
    cup_needed_litters = cups.popleft()

    if bottle_litters >= cup_needed_litters:
        wasted_litters_of_water += bottle_litters - cup_needed_litters
    else:
        cups.appendleft(cup_needed_litters - bottle_litters)

if bottles:
    bottles.reverse()
    print("Bottles: ", end='')
    print(*bottles, sep=' ')
elif cups:
    print("Cups: ", end='')
    print(*cups, sep=' ')

print(f"Wasted litters of water: {wasted_litters_of_water}")
