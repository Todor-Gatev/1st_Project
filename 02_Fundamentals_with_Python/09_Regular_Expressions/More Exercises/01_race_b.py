import re

participants = {x: 0 for x in input().split(", ")}

name_reg = re.compile(r"[A-Za-z]")
distance_reg = re.compile(r"\d")

while True:
    info = input()

    if info == "end of race":
        break

    name = ''.join(name_reg.findall(info))
    distance = sum([int(x) for x in distance_reg.findall(info)])

    if name in participants:
        participants[name] += distance

participants = sorted(participants.items(), key=lambda x: -x[1])

print(f"1st place: {participants[0][0]}")
print(f"2nd place: {participants[1][0]}")
print(f"3rd place: {participants[2][0]}")
