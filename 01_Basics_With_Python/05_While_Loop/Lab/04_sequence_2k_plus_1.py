# Read user input
input_number = int(input())

# Logic
current_number = 1

while True:
    if current_number > input_number:
        break
    print(current_number)
    current_number = 2 * current_number + 1

# Print Output
