clothes = [int(x) for x in input().split()]
rack_capacity = int(input())
racks = 1
free_capacity = rack_capacity

while clothes:
    if free_capacity < clothes[-1]:
        free_capacity = rack_capacity
        racks += 1
        continue

    free_capacity -= clothes.pop()

print(racks)
