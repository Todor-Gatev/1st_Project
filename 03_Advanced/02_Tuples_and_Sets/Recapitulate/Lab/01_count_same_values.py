nums = tuple(float(x) for x in input().split())
unique_nums = set(nums)

print(unique_nums)

for num in unique_nums:
    print(f"{num:.1f} - {nums.count(num)} times")
