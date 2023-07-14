# Read user input
town = input()
package = input()
vip = input()
days = int(input())

# Parameters

# Variables
price = 0
is_valid = True

# Logic
if days > 7:
    days -= 1

if days < 1:
    print("Days must be positive number!")
elif town == 'Bansko' or town == 'Borovets':
    if package == 'noEquipment':
        if vip == 'yes':
            price = days * 80 * (1 - 0.05)
        elif vip == 'no':
            price = days * 80
        else:
            is_valid = False
    elif package == 'withEquipment':
        if vip == 'yes':
            price = days * 100 * (1 - 0.10)
        elif vip == 'no':
            price = days * 100
        else:
            is_valid = False
    else:
        is_valid = False
elif town == 'Varna' or town == 'Burgas':
    if package == 'noBreakfast':
        if vip == 'yes':
            price = days * 100 * (1 - 0.07)
        elif vip == 'no':
            price = days * 100
        else:
            is_valid = False
    elif package == 'withBreakfast':
        if vip == 'yes':
            price = days * 130 * (1 - 0.12)
        elif vip == 'no':
            price = days * 130
        else:
            is_valid = False
    else:
        is_valid = False
else:
    is_valid = False
# End of Logic

# Print Output
if not is_valid:
    print("Invalid input!")
elif price > 0:
    print(f'The price is {price:.2f}lv! Have a nice time!')
