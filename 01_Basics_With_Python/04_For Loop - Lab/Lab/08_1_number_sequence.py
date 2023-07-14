# Read user input
number_of_iterations = int(input())

# Logic
min_number = 0
max_number = 0

for i in range(1, number_of_iterations + 1):
    current_number = int(input())
    if i == 1:
        max_number = current_number
        min_number = current_number
    else:
        if current_number > max_number:
            max_number = current_number
        if min_number > current_number:
            min_number = current_number

# Print Output
print(f'Max number: {max_number}')
print(f'Min number: {min_number}')
