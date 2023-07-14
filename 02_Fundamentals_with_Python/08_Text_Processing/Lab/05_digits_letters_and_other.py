text = input()

digits = ""
letters = ""
characters = ""

for ch in text:
    if ch.isdigit():
        digits += ch
    elif ch.isalpha():
        letters += ch
    else:
        characters += ch

print(digits)
print(letters)
print(characters)
