import re

participants = input().split(", ")
command = input()

racers_dict = {}
name_reg = re.compile(r"[A-Za-z]+")

while command != "end of race":
    name = ''.join(name_reg.findall(command))
    if name in participants:
        if name not in racers_dict:
            racers_dict[name] = 0
        distance = 0
        for ch in command:
            if ch.isdigit():
                distance += int(ch)

        racers_dict[name] += distance
    command = input()

# result = sorted(racers_dict.items(), key=lambda x: (-x[1], x[0]))
result = sorted(racers_dict.items(), key=lambda x: -x[1])


print(f"1st place: {result[0][0]}")
print(f"2nd place: {result[1][0]}")
print(f"3rd place: {result[2][0]}")
