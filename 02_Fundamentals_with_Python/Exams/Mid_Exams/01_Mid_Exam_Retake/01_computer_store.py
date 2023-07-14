# Read user input
command = input()

# Variables
total_price_without_taxes = 0

# Logic
while command != "special" and command != "regular":

    if float(command) < 0:
        print("Invalid price!")
        command = input()
        continue

    total_price_without_taxes += float(command)
    command = input()

taxes = total_price_without_taxes * 0.2
total_price = total_price_without_taxes + taxes

if command == "special":
    total_price *= 0.9
# End of Logic

# Print Output
if total_price_without_taxes == 0:
    print("Invalid order!")
else:
    print("Congratulations you've just bought a new computer!")
    print(f"Price without taxes: {total_price_without_taxes:.2f}$")
    print(f"Taxes: {taxes:.2f}$")
    print("-----------")
    print(f"Total price: {total_price:.2f}$")
