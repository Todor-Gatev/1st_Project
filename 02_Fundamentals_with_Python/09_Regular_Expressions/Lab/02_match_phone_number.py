import re

text = input()

# pattern = r"\+359 2 \d{3} \d{4}\b|\+359-2-\d{3}-\d{4}\b"
#
# num = re.findall(pattern, text)
# print(*num, sep=', ')

# solution 2

pattern = r"\+359([\s-])2\1\d{3}\1\d{4}\b"
results = re.finditer(pattern, text)
nums = []

for res in results:
    nums.append(res.group())


print(*nums, sep=", ")
