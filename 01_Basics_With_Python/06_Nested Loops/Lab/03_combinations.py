# Read user input
input_number = int(input())

# Logic
count_combinations = 0
for x1 in range(input_number + 1):
    for x2 in range(input_number + 1):
        for x3 in range(input_number + 1):
            if x1 + x2 + x3 == input_number:
                count_combinations += 1
else:
    print(count_combinations)

# End of Logic

# Print Output

# TODO: Add logic here
# TODO: Check the other cases…
