# TODO: Use recursion.
#  exercise 03_Advanced/07_File_Handling/Exercises/04-Directory-Traversal_a
#  Dido video Advanced January 2023
#
# def recursive_power(num, power):
#     if power == 0:
#         return 1
#     return num * recursive_power(num, power - 1)
#
#
# print(recursive_power(2, 0))  # 1024
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

    if word[idx] != word[-idx-1]:
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
