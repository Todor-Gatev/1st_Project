def is_palindrome(text):
    for i in range(len(text) // 2):
        if text[i] != text[-i - 1]:
            return False
    else:
        return True


# Read user input
user_str_list = input().split(', ')

# Logic
for el in user_str_list:
    print(is_palindrome(el))

# Print Output
