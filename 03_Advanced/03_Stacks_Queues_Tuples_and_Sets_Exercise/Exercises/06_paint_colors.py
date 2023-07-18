from collections import deque

deque_of_strings = deque(input().split())
colors = ["red", "yellow", "blue", "orange", "purple", "green"]
main_colors = {"red", "yellow", "blue"}
slave_colors = {"orange", "purple", "green"}
found_colors = []

map_function = {
    "orange": lambda x: {"red", "yellow"}.issubset(found_colors),
    "purple": lambda x: {"red", "blue"}.issubset(found_colors),
    "green": lambda x: {"blue", "yellow"}.issubset(found_colors),
}

while deque_of_strings:
    str1 = deque_of_strings.popleft()
    str2 = deque_of_strings.pop() if deque_of_strings else ""

    if str1 + str2 in colors:
        found_colors.append(str1 + str2)
    elif str2 + str1 in colors:
        found_colors.append(str2 + str1)
    else:
        if len(str2) > 1:
            deque_of_strings.insert(len(deque_of_strings) // 2, str2[:-1])

        if len(str1) > 1:
            deque_of_strings.insert(len(deque_of_strings) // 2, str1[:-1])

if main_colors.issubset(found_colors):
    print(found_colors)
else:
    for idx in range(len(found_colors) - 1, -1, -1):
        if found_colors[idx] in slave_colors:
            if not map_function[found_colors[idx]](None):
                found_colors.pop(idx)

    print(found_colors)
