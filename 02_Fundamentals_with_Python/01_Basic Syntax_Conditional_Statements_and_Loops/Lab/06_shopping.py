# Read user input
budget = int(input())

# Logic
while budget >= 0:
    user_input = input()

    if user_input == 'End':
        print("You bought everything needed.")
        break

    budget -= int(user_input)
else:
    print("You went in overdraft!")
# End of Logic

# Print Output
