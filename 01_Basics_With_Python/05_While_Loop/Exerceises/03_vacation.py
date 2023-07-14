# Read user input
vacation_price = float(input())
available_funds = float(input())

# Logic
days_counter = 0
spend_money_days_counter = 0

while True:
    spend_or_save = input()
    amount = float(input())
    days_counter += 1
    
    if spend_or_save == 'spend':
        spend_money_days_counter += 1
        if spend_money_days_counter == 5:
            print(f'You can\'t save the money.')
            print(days_counter)
            break
        elif amount > available_funds:
            available_funds = 0
        else:
            available_funds -= amount
    else:
        available_funds += amount
        spend_money_days_counter = 0

    if available_funds >= vacation_price:
        print(f'You saved the money for {days_counter} days.')
        break

# Print Output
