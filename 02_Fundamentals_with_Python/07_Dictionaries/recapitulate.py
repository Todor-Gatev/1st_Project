nums = [int(x) for x in input().split()]
avg_num = sum(nums) / len(nums)
# result = []

# for el in nums:
#     if el > avg_num:
#         result.append(el)

result = list(filter(lambda x: x > avg_num, nums))

if result:
    result.sort(reverse=True)
    i = min(5, len(result))
    for j in range(i):
        print(result[j], end=' ')
else:
    print("No")
