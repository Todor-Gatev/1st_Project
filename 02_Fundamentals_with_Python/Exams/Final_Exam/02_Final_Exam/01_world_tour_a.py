stops = input()

while True:
    command = input()

    if command == "Travel":
        break

    action, *info = command.split(':')

    if action == "Add Stop":
        idx, str_ = int(info[0]), info[1],

        if idx in range(len(stops)):
            stops = stops[:idx] + str_ + stops[idx:]
    elif action == "Remove Stop":
        start_idx, end_idx = int(info[0]), int(info[1]),

        if start_idx in range(len(stops)) and end_idx in range(len(stops)):
            stops = stops[:start_idx] + stops[end_idx + 1:]
    elif action == "Switch":
        old_str, new_str = info[0], info[1]
        stops = stops.replace(old_str, new_str)

    print(stops)

print(f"Ready for world tour! Planned stops: {stops}")
