# Read user input
route = input().split("||")
fuel = int(input())
ammunition = int(input())

# Logic
for el in route:
    if el == "Titan":
        print("You have reached Titan, all passengers are safe.")
        exit()

    action, amount = el.split()
    amount = int(amount)

    if action == "Travel":
        if fuel < amount:
            print("Mission failed.")
            exit()

        fuel -= amount
        print(f"The spaceship travelled {amount} light-years.")
    elif action == "Enemy":
        if ammunition >= amount:
            ammunition -= amount
            print(f"An enemy with {amount} armour is defeated.")
        else:
            if fuel >= 2 * amount:
                print(f"An enemy with {amount} armour is outmaneuvered.")
                fuel -= 2 * amount
            else:
                print("Mission failed.")
                exit()
    elif action == "Repair":
        fuel += amount
        ammunition += 2 * amount
        print(f"Ammunitions added: {2 * amount}.")
        print(f"Fuel added: {amount}.")
        pass
# End of Logic
