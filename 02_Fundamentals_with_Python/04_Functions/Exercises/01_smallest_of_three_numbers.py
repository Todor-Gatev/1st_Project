def min_num(numbers: []):
    result = min(numbers)

    return result


n = 3
user_nums = []

for i in range(n):
    user_nums.append(int(input()))

print(min_num(user_nums))
