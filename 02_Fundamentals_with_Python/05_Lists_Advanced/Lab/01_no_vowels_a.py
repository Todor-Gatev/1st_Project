def remove_forbidden_chars(text):
    forbidden_chars = ['a', 'o', 'u', 'e', 'i']
    result = [ch for ch in text if ch.lower() not in forbidden_chars]
    return ''.join(result)


# Read user input
usr_text = input()


# Logic
# no_vowels = [ch for ch in text if ch.lower() not in forbidden_chars]
# for ch in text:
#     if ch.lower() not in ['a', 'o', 'u', 'e', 'i']:
#         no_vowels.append(ch)

# Print Output
# print(''.join(no_vowels))
print(remove_forbidden_chars(usr_text))
