def level_bar(percent):
    level = str(percent) \
        + '% ' \
        + '[' \
        + int(percent / 10) * '%' \
        + int(10 - (percent / 10)) * '.' \
        + ']'

    return level


level_num = int(input())

if level_num == 100:
    print("100% Complete!")
    print("[%%%%%%%%%%]")
else:
    print(level_bar(level_num))
    print("Still loading...")
