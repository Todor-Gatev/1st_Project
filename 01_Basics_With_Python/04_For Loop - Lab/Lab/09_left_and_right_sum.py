# Read user input
num = int(input())

# Logic
# num_of_numbers = 2 * num
first_sum = 0
second_sum = 0

for i in range(2 * num):
    input_number = int(input())
    if i < num:
        first_sum += input_number
    else:
        second_sum += input_number

diff = abs(first_sum - second_sum)

if first_sum == second_sum:
    print(f'Yes, sum = {first_sum}')
else:
    print(f'No, diff = {diff}')

# Print Output
