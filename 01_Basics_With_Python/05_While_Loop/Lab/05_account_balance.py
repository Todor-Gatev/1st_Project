# Read user input

# Logic
total_amount = 0

while True:
    customer_input = input()
    if customer_input == 'NoMoreMoney':
        break

    income = float(customer_input)

    if income < 0:
        print('Invalid operation!')
        break

    total_amount += income
    print(f'Increase: {income:.2f}')

# Print Output
print(f'Total: {total_amount:.2f}')
