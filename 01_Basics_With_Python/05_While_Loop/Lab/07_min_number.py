from sys import maxsize
# Read user input

# Logic
min_number = maxsize
while True:
    input_variable = input()
    if input_variable == "Stop":
        print(min_number)
        break
    current_number = int(input_variable)
    if current_number < min_number:
        min_number = current_number

# Print Output
