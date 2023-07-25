import re

attacked, destroyed = [], []

star_regex = re.compile(r"[star]", re.IGNORECASE)

info_regex = re.compile(r"@(?P<name>[A-Za-z]+)"
                        r"[^-@!:>]*"
                        r":(\d+)"
                        r"[^-@!:>]*"
                        r"!(?P<attack>[AD])!"
                        r"[^-@!:>]*"
                        r"->(\d+)")

for _ in range(int(input())):
    message = input()
    count_star = len(star_regex.findall(message))
    decipher = ""

    for ch in message:
        decipher += chr(ord(ch) - count_star)

    result = info_regex.search(decipher)

    if result:
        if result.group("attack") == 'A':
            attacked.append(result.group("name"))
        elif result.group("attack") == 'D':
            destroyed.append(result.group("name"))


print(f"Attacked planets: {len(attacked)}")

if attacked:
    attacked.sort()
    print("-> ", end='')
    print(*attacked, sep="\n-> ")

print(f"Destroyed planets: {len(destroyed)}")

if destroyed:
    destroyed.sort()
    print("-> ", end='')
    print(*destroyed, sep="\n-> ")
