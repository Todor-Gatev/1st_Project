import re
# from math import prod

text = input()

coolness = 1
coolness_list = [int(x) for x in re.findall(r"\d", text)]
for num in coolness_list:
    coolness *= num

cool_emoji = []
count_emoji = 0
# (?P<sep>:{2}|\*{2})(?P<emoji>[A-Z][a-z]{2,})(?P=sep)
result = re.finditer(r"(?P<sep>:{2}|\*{2})(?P<emoji>[A-Z][a-z]{2,})(?P=sep)", text)

for res in result:
    count_emoji += 1
    emoji = res.group("emoji")
    emoji_coolness = 0
    for ch in emoji:
        emoji_coolness += ord(ch)

    if emoji_coolness > coolness:
        cool_emoji.append(res.group())

print(f"Cool threshold: {coolness}")
print(f"{count_emoji} emojis found in the text. The cool ones are:")
print(*cool_emoji, sep='\n')
