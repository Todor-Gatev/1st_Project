def is_palindrome(a):
    half = len(a) // 2

    for i in range(half):
        if a[i] != a[-i - 1]:
            return False

    return True


user_nums_as_str = input().split(', ')

for num_as_str in user_nums_as_str:
    print(is_palindrome(num_as_str))
