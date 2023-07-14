# Read user input
budget = float(input())
ticket_class = input()
persons = int(input())

# Parameters

# Variables
vip_ticket_price = 499.99
normal_ticket_price = 249.99
transport_price = 0
tickets_price = 0
needed_money = 0

# Logic
if persons < 5:
    transport_price = 0.75 * budget
elif persons < 10:
    transport_price = 0.60 * budget
elif persons < 25:
    transport_price = 0.50 * budget
elif persons < 50:
    transport_price = 0.40 * budget
else:
    transport_price = 0.25 * budget

if ticket_class == 'VIP':
    tickets_price = persons * vip_ticket_price
elif ticket_class == 'Normal':
    tickets_price = persons * normal_ticket_price

needed_money = transport_price + tickets_price
diff_price = budget - needed_money
# End of Logic

# Print Output
if diff_price >= 0:
    print(f'Yes! You have {diff_price:.2f} leva left.')
else:
    print(f'Not enough money! You need {-diff_price:.2f} leva.')
