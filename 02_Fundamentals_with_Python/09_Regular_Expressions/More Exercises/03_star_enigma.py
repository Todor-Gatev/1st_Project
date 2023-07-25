import re

num_messages = int(input())

# @(?P<planet>[A-Za-z]+)[^@!:>-]*:(?P<population>\d+)[^@!:>-]*!(?P<action>[AD])![^@!:>-]*->\d+
key_regex = re.compile(r"[star]")
regex = re.compile(r"@(?P<planet>[A-Za-z]+)"
                   r"[^@!:>-]*"
                   r":(?P<population>\d+)"
                   r"[^@!:>-]*"
                   r"!(?P<action>[AD])!"
                   r"[^@!:>-]*"
                   r"->\d+")

attacked_planets = []
destroyed_planets = []

for _ in range(num_messages):
    message = input()
    key = len(key_regex.findall(message.casefold()))
    decrypted_message = ""

    for ch in message:
        decrypted_message += chr(ord(ch) - key)

    result = regex.finditer(decrypted_message)

    for res in result:
        if res.group("action") == "A":
            attacked_planets.append(res.group("planet"))
        else:
            destroyed_planets.append(res.group("planet"))

print(f"Attacked planets: {len(attacked_planets)}")

if attacked_planets:
    attacked_planets.sort()

    for planet in attacked_planets:
        print(f"-> {planet}")
#
print(f"Destroyed planets: {len(destroyed_planets)}")

if destroyed_planets:
    destroyed_planets.sort()

    for planet in destroyed_planets:
        print(f"-> {planet}")
