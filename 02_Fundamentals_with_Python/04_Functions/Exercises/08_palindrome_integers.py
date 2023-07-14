def is_palindrome(a):
    half = len(a) // 2
    if len(a) % 2 == 0:
        first_half_str = a[:half]
        second_half_str = a[half:]
    else:
        first_half_str = a[:half]
        second_half_str = a[half + 1:]

    for i in range(half):
        if first_half_str[i] != second_half_str[-i - 1]:
            return False

    return True


user_nums_as_str = input().split(', ')

for num_as_str in user_nums_as_str:
    print(is_palindrome(num_as_str))
