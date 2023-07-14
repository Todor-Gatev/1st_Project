import re


text = input().casefold()
word = input().casefold()

pattern = rf'\b{word}\b'

# matches = re.findall(rf'(^|(?<=\s)){word}($|(?=\s))', text)
matches = re.findall(rf'\b{word}\b', text)

print(len(matches))
