# Read user input
clothes = list(map(int, input().split()))
rack_capacity = int(input())

left_capacity = 0
racks_num = 0

while clothes:
    if left_capacity < clothes[-1]:
        left_capacity = rack_capacity
        racks_num += 1

    left_capacity -= clothes.pop()

print(racks_num)
