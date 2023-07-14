# Variables
composite_num_sum = 0
prime_num_sum = 0

# Logic
while True:
    user_input = input()

    if user_input == 'stop':
        break

    current_num = int(user_input)

    if current_num < 0:
        print("Number is negative.")
        continue

    is_prime = True
    for i in range(2, current_num):
        if current_num % i == 0:
            composite_num_sum += current_num
            is_prime = False
            break

    if is_prime:
        prime_num_sum += current_num
# End of Logic

# Print Output
print(f'Sum of all prime numbers is: {prime_num_sum}')
print(f'Sum of all non prime numbers is: {composite_num_sum}')
