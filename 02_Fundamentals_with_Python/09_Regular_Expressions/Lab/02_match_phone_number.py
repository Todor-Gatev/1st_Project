import re

text1 = input()

pattern = r"\+359 2 \d{3} \d{4}\b|\+359-2-\d{3}-\d{4}\b"

num1 = re.findall(pattern, text1)
print(*num1, sep=', ')
