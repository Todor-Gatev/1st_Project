clothes = [int(x) for x in input().split()]
capacity = int(input())

hangs_pcs = 1
total_sum = 0

while clothes:
    if clothes[-1] + total_sum > capacity:
        hangs_pcs += 1
        total_sum = 0

    total_sum += clothes[-1]
    clothes.pop()

print(hangs_pcs)
