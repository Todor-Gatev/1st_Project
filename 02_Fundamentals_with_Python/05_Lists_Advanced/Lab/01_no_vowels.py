# Read user input
text = input()

forbidden_letters = ['a', 'o', 'u', 'e', 'i']

# Logic
no_vowels = [ch for ch in text if ch.lower() not in forbidden_letters]
# for ch in text:
#     if ch.lower() not in ['a', 'o', 'u', 'e', 'i']:
#         no_vowels.append(ch)

# Print Output
print(''.join(no_vowels))
