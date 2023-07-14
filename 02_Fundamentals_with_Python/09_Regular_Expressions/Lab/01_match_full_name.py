import re

names = input()

pattern = r"\b[A-Z][a-z]+ [A-Z][a-z]+\b"

matches = re.findall(pattern, names)
print(*matches)
if re.findall(pattern, names):
    print("yes")
else:
    print("no")

matches = re.match(pattern, names)
print(matches)
if re.match(pattern, names):
    print("yes")
else:
    print("no")
