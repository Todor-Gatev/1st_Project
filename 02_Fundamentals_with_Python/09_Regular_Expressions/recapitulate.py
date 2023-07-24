import re

star_regex = re.compile(r"[star]", re.IGNORECASE)

for _ in range(int(input())):
    message = input()
    count_star = len(star_regex.findall(message))
    decipher = ""
    for ch in message:
        decipher += chr(ord(ch) - count_star)

    print(decipher)

