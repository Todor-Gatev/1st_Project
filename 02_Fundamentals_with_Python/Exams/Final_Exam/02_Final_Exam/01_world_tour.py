tour = input()

command = input()

while command != "Travel":
    command = command.split(':')
    action = command[0]
    if action == "Add Stop":
        idx = int(command[1])
        if idx in range(len(tour)):
            tour = tour[:idx] + command[2] + tour[idx:]
        print(tour)
    elif action == "Remove Stop":
        start_idx = int(command[1])
        end_idx = int(command[2])
        if start_idx in range(len(tour)) and end_idx in range(len(tour)):
            idx1 = min(start_idx, end_idx)
            idx2 = max(start_idx, end_idx)
            tour = tour[:idx1] + tour[idx2 + 1:]
        print(tour)
    elif action == "Switch":
        if command[1] in tour:
            tour = tour.replace(command[1], command[2])
        print(tour)
    command = input()

print(f"Ready for world tour! Planned stops: {tour}")
