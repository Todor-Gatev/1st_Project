# Read user input
day_of_the_week = input()
ticket_price = 0


# Logic
if day_of_the_week == "Wednesday" \
        or day_of_the_week == "Thursday":
    ticket_price = 14
elif day_of_the_week == "Saturday" \
        or day_of_the_week == "Sunday":
    ticket_price = 16
else:
    ticket_price = 12

# Print Output
print(ticket_price)
