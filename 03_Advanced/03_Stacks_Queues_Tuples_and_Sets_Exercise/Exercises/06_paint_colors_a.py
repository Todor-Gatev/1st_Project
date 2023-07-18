from collections import deque

deque_of_strings = deque(input().split())
colors = {"red", "yellow", "blue", "orange", "purple", "green"}
main_colors = {"red", "yellow", "blue"}
slave_colors = {"orange", "purple", "green"}
found_colors = []

map_colors = {
    "orange": {"red", "yellow"},
    "purple": {"red", "blue"},
    "green": {"blue", "yellow"}
}

while deque_of_strings:
    str1 = deque_of_strings.popleft()
    str2 = deque_of_strings.pop() if deque_of_strings else ""

    if str1 + str2 in colors:
        found_colors.append(str1 + str2)
    elif str2 + str1 in colors:
        found_colors.append(str2 + str1)
    else:
        for el in (str2[:-1], str1[:-1]):
            if el:
                deque_of_strings.insert(len(deque_of_strings) // 2, el)

if main_colors.issubset(found_colors):
    print(found_colors)
else:
    for color in set(map_colors.keys()).intersection(found_colors):
        if not map_colors[color].issubset(found_colors):
            while color in found_colors:
                found_colors.remove(color)

    print(found_colors)
