# # recursion is time and space consuming - can be used when there is dictionary in dictionary...unknown times

# def a():  # infinite recursion
#     a()
#
#
# a()  # [Previous line repeated 996 more times]
# # RecursionError: maximum recursion depth exceeded

# def recursive_power(num, power):  # short but not good for debugging
#     if power == 0:
#         return 1
#     return num * recursive_power(num, power - 1)

def recursive_power(number, power):  # longer but in debug you can see how recursion works
    result = 1
    if power == 0:
        return result
    result = number * recursive_power(number, power - 1)
    return result
    # return number ** power


print(recursive_power(2, 3))


#
#
# print(recursive_power(2, 0))  # 1
# # print(recursive_power(2, 10))  # 1024

# def factorial(num):
#     if not isinstance(num, int) or num < 0:
#         return f"Sorry. '{num}' is incorrect."
#
#     if num == 1:
#         return 1
#
#     return num * factorial(num - 1)
#
#
# print(factorial(5))  # 120
# print(factorial(6))  # 720
# print(factorial(-5))  # Sorry. 'number' is incorrect.
# print(factorial('z'))  # Sorry. 'number' is incorrect.

def palindrome(word, idx):
    if idx == len(word) // 2:
        return f"{word} is a palindrome"

    if word[idx] != word[-idx - 1]:
        return f"{word} is not a palindrome"

    return palindrome(word, idx + 1)


# print(palindrome("abcba", 0))
print(palindrome("abcdcba", 0))
# print(palindrome("peter", 0))


# def not_recursion():
#     def not_recursion():
#         def not_recursion():
#             print(3)
#
#         print(2)
#         not_recursion()
#
#     print(1)
#     not_recursion()
#
# not_recursion()
