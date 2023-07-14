# Read user input
destination = input()
min_budget = float(input())

saved_money = 0.0

# Logic
while destination != 'End':
    while True:
        if saved_money >= min_budget:
            print(f"Going to {destination}!")
            saved_money = 0.0
            break
        current_savings = float(input())
        saved_money += current_savings

    destination = input()
    if destination == 'End':
        break
    min_budget = float(input())

# End of Logic

# Print Output

# # TODO: Add logic here
# TODO: Check the other cases…
