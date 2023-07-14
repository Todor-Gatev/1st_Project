from sys import maxsize
# Read user input

# Logic
max_number = - maxsize
while True:
    input_variable = input()
    if input_variable == "Stop":
        print(max_number)
        break
    current_number = int(input_variable)
    if current_number > max_number:
        max_number = current_number

# Print Output
