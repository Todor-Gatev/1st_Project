# Read user input
num = int(input())

# Logic
max_num = 0
total_sum = 0
for i in range(num):
    current_num = int(input())
    total_sum += current_num
    if i == 0:
        max_num = current_num
    elif max_num < current_num:
        max_num = current_num

rest_num_sum = total_sum - max_num
diff = abs(rest_num_sum - max_num)

if rest_num_sum == max_num:
    print('Yes')
    print(f'Sum = {max_num}')
else:
    print('No')
    print(f'Diff = {diff}')

# Print Output
