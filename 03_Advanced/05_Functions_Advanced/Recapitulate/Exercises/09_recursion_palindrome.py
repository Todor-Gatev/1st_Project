def palindrome(word, idx):
    if word[idx] != word[-1 - idx]:
        return f"{word} is not a palindrome"
    elif idx == len(word) // 2:
        return f"{word} is a palindrome"

    return palindrome(word, idx + 1)


# print(palindrome("abcba", 0))
# print(palindrome("peter", 0))
print(palindrome("peterep", 0))
