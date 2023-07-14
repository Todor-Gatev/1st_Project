import sys

# Read user input
number_of_iterations = int(input())

# Logic
max_number = -sys.maxsize  # -2147483647
min_number = sys.maxsize  # 2147483647

for _ in range(number_of_iterations):
    current_number = int(input())
    if max_number < current_number:
        max_number = current_number
    if min_number > current_number:
        min_number = current_number

# Print Output
print(f'Max number: {max_number}')
print(f'Min number: {min_number}')

# import sys
# print(sys.maxsize)    # 2147483647
# print(-sys.maxsize)   # -2147483647
