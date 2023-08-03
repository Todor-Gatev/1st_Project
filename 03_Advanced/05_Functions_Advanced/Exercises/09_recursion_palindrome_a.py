def palindrome(text, idx):
    if idx == len(text) // 2:
        return f"{text} is a palindrome"
    elif text[idx] != text[-idx - 1]:
        return f"{text} is not a palindrome"

    return palindrome(text, idx + 1)


# print(palindrome("abcba", 0))
print(palindrome("peterp", 0))
