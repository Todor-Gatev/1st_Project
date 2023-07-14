# Read user input
budget = float(input())
flour_price_kg = float(input())

# Parameters
eggs_price_per_loave = 0.75 * flour_price_kg
milk_price_per_loave = 1.25 * flour_price_kg / 4
loave_price = flour_price_kg + eggs_price_per_loave + milk_price_per_loave
loaves_pcs = int(budget // loave_price)
money_left = budget % loave_price

# Variables
colored_eggs = 0

# Logic
for i in range(1, loaves_pcs + 1):
    colored_eggs += 3

    if i % 3 == 0:
        colored_eggs_lost = i - 2
        colored_eggs -= colored_eggs_lost
        if colored_eggs < 0:
            colored_eggs = 0
# End of Logic

# Print Output
print(f"You made {loaves_pcs} loaves of Easter bread! Now you have "
      f"{colored_eggs} eggs and {money_left:.2f}BGN left.")
