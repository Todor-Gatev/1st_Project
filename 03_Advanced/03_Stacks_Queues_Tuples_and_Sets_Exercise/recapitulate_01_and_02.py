from collections import deque

strings = deque(input().split())

collected_colors = []
main_colors = {"red", "yellow", "blue"}
secondary_colors = {
    "orange": {"red", "yellow"},
    "purple": {"red", "blue"},
    "green": {"yellow", "blue"},
}

while strings:
    str1 = strings.popleft()
    str2 = strings.pop() if strings else ""

    if str1 + str2 in main_colors.union(secondary_colors):
        collected_colors.append(str1 + str2)
    elif str2 + str1 in main_colors.union(secondary_colors):
        collected_colors.append(str2 + str1)
    else:
        for el in (str2, str1):
            if el:
                strings.insert(int(len(strings) / 2), el[:-1])

if main_colors.issubset(collected_colors):
    print(collected_colors)
else:
    for color in set(collected_colors).intersection(secondary_colors):
        if not secondary_colors[color].issubset(collected_colors):
            while color in collected_colors:
                collected_colors.remove(color)

    print(collected_colors)
