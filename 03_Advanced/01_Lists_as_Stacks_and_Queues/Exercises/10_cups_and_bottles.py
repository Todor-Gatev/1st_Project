from collections import deque

cups = deque(int(x) for x in input().split())
bottles = [int(x) for x in input().split()]

wasted_litters_of_water = 0
is_cup_in_progress = False
cup_needed_litters = 0
last_cup = 0

while cups and bottles:
    bottle_litters = bottles.pop()

    if not is_cup_in_progress:
        last_cup = cup_needed_litters = cups.popleft()

    if bottle_litters >= cup_needed_litters:
        wasted_litters_of_water += bottle_litters - cup_needed_litters
        is_cup_in_progress = False
    else:
        cup_needed_litters -= bottle_litters
        is_cup_in_progress = True

if is_cup_in_progress:
    cups.appendleft(cup_needed_litters)

if bottles:
    bottles.reverse()
    print("Bottles: ", end='')
    print(*bottles, sep=' ')
elif cups:
    print("Cups: ", end='')
    print(*cups, sep=' ')
elif is_cup_in_progress:
    print(f"Cups: {cup_needed_litters}")

print(f"Wasted litters of water: {wasted_litters_of_water}")
