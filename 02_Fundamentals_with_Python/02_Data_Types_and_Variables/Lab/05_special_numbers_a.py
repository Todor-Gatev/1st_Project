# Read user input
n = int(input())

# Logic
for i in range(1, n + 1):
    sum_digits = 0
    is_special = False
    number = i

    while number:
        digit = number % 10
        sum_digits += digit
        number = number // 10
        # number = int(number / 10)

    if sum_digits == 5 or \
            sum_digits == 7 or \
            sum_digits == 11:
        is_special = True

    print(f"{i} -> {is_special}")
