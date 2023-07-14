# from sys import maxsize

# Read user input
n_num = int(input())

# Parameters

# Variables
odd_sum, even_sum = 0, 0
odd_min, even_min = 'No', 'No'
odd_max, even_max = 'No', 'No'

# Logic
for i in range(1, n_num + 1):
    current_num = float(input())

    if i == 1:
        odd_max = odd_min = current_num
        odd_sum += current_num
    elif i == 2:
        even_max = even_min = current_num
        even_sum += current_num
    elif i % 2 != 0:
        odd_sum += current_num
        if current_num > odd_max:
            odd_max = current_num
        if current_num < odd_min:
            odd_min = current_num
    else:
        even_sum += current_num
        if current_num > even_max:
            even_max = current_num
        if current_num < even_min:
            even_min = current_num
# End of Logic

# Print Output
print(f'OddSum={odd_sum:.2f},')

if n_num < 1:
    print(f'OddMin={odd_min},')
    print(f'OddMax={odd_max},')
else:
    print(f'OddMin={odd_min:.2f},')
    print(f'OddMax={odd_max:.2f},')

print(f'EvenSum={even_sum:.2f},')

if n_num < 2:
    print(f'EvenMin={even_min},')
    print(f'EvenMax={even_max}')
else:
    print(f'EvenMin={even_min:.2f},')
    print(f'EvenMax={even_max:.2f}')
