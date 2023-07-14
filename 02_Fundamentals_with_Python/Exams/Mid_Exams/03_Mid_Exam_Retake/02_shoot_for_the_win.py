# Read user input
integers = [int(x) for x in input().split()]
command = input()

# Variables

# Logic
while command != "End":
    idx = int(command)

    if idx >= len(integers):
        command = input()
        continue

    shot = integers[idx]

    if shot == -1:
        command = input()
        continue

    for i in range(len(integers)):
        num = integers[i]
        if num == -1 or i == idx:
            continue

        if shot < num:
            integers[i] -= shot
        else:
            integers[i] += shot

    integers[idx] = -1
    command = input()
# End of Logic

# Print Output
count = len(list(filter(lambda x: x == -1, integers)))
print(f"Shot targets: {count} -> ", end='')
print(*integers, sep=' ')
