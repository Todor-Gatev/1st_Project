# Read user input
start_number = int(input())
final_number = int(input())
magic_number = int(input())

# Logic
combinations_counter = 0
combination_is_found = False

for i in range(start_number, final_number + 1):
    for j in range(start_number, final_number + 1):
        combinations_counter += 1
        if i + j == magic_number:
            combination_is_found = True
            print(f"Combination N:{combinations_counter} ({i} + {j} = {magic_number})")
            break

    if combination_is_found:
        break

else:
    print(f"{combinations_counter} combinations - neither equals {magic_number}")

# End of Logic

# Print Output

# TODO: Add logic here
# TODO: Check the other cases…
