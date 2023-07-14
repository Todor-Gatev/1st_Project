# Read user input
words = input().split()
palindrome = input()

# Variables
found_palindromes = []

# Logic
for word in words:
    # reversed_list = reversed(word)
    # reversed_word = "".join(reversed_list)
    reversed_word = word[::-1]
    if reversed_word == word:
        found_palindromes.append(word)
    # for i in range(len(word) // 2):
    #     if word[i] != word[-i - 1]:
    #         break
    # else:
    #     found_palindromes.append(word)

number = found_palindromes.count(palindrome)
# End of Logic

# Print Output
print(found_palindromes)
print(f"Found palindrome {number} times")
