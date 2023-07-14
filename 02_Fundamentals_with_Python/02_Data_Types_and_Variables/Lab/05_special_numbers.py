# Read user input
n = int(input())

# Logic
for i in range(1, n + 1):
    sum_digits = 0
    is_special = False
    str_i = str(i)

    for j in str_i:
        int_j = int(j)
        sum_digits += int_j

    if sum_digits == 5 or sum_digits == 7 or sum_digits == 11:
        is_special = True

    print(f"{i} -> {is_special}")
# End of Logic
