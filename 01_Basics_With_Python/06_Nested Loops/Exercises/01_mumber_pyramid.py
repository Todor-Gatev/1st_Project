# Read user input
input_number = int(input())

# Logic
min_counter = 1
max_counter = 2
counter = 1
current_num = 1
not_all_is_printed_yet = current_num <= input_number

while not_all_is_printed_yet:
    for current_num in range(min_counter, max_counter):
        # current_num = j
        not_all_is_printed_yet = current_num <= input_number
        if not_all_is_printed_yet:
            print(current_num, end=' ')
    print()
    counter += 1
    min_counter = max_counter
    max_counter += counter

# End of Logic

# Print Output

# TODO: Add logic here
# TODO: Check the other cases…
