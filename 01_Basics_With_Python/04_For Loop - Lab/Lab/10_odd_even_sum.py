# Read user input
num = int(input())

# Logic
even_num_sum = 0
odd_num_sum = 0

for i in range(1, num+1):
    input_number = int(input())
    if i % 2 == 0:
        even_num_sum += input_number
    else:
        odd_num_sum += input_number

diff = abs(even_num_sum - odd_num_sum)

if diff == 0:
    print('Yes')
    print(f'Sum = {even_num_sum}')
else:
    print('No')
    print(f'Diff = {diff}')

# Print Output

