import re

participants = input().split(", ")
race_info = {}
name_regex = re.compile(r"[A-Za-z]")
dist_regex = re.compile(r"\d")

while True:
    text = input()

    if text == "end of race":
        break

    name = ''.join(name_regex.findall(text))
    if name in participants:
        if name not in race_info:
            race_info[name] = 0

        distance = sum(list(map(int, dist_regex.findall(text))))
        race_info[name] += distance

race_info = sorted(race_info, key=lambda x: -race_info[x])
print(f"1st place: {race_info[0]}")
print(f"2nd place: {race_info[1]}")
print(f"3rd place: {race_info[2]}")
