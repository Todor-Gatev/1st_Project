from collections import deque

cups = deque(int(x) for x in input().split())
bottles = [int(x) for x in input().split()]

wasted_water = 0
is_cup_full = True

while cups and bottles:
    bottle_liters = bottles.pop()
    cup_needed_liters = cups[0] if is_cup_full else cup_needed_liters

    if cup_needed_liters > bottle_liters:
        is_cup_full = False
        cup_needed_liters -= bottle_liters
    else:
        is_cup_full = True
        cups.popleft()
        wasted_water += bottle_liters - cup_needed_liters

if cups:
    print("Cups:", *cups)
else:
    print("Bottles:", *reversed(bottles))

print(f"Wasted litters of water: {wasted_water}")
