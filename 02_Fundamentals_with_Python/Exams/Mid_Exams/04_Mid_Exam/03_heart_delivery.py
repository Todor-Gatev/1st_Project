# Read user input
integers = [int(x) for x in input().split('@')]
command = input()

# Variables
idx = 0

# Logic
while command != "Love!":
    length = command.split()[1]
    idx += int(length)

    if idx >= len(integers):
        idx = 0

    if integers[idx] == 0:
        print(f"Place {idx} already had Valentine's day.")
    else:
        integers[idx] -= 2
        if integers[idx] == 0:
            print(f"Place {idx} has Valentine's day.")

    command = input()
# End of Logic

# Print Output
print(f"Cupid's last position was {idx}.")

if max(integers) == 0:
    print("Mission was successful.")
else:
    failed = list(filter(lambda x: x != 0, integers))
    houseCount = len(failed)
    print(f"Cupid has failed {houseCount} places.")
