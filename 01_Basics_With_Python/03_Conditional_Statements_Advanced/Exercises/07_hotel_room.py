# Read user input
month = input()
overnight_stays = int(input())

# Logic
room_price = 0
apartment_price = 0
discount_room = 0
discount_apart = 0

if month == "May" or month == "October":
    room_price = 50
    apartment_price = 65
    if overnight_stays > 14:
        discount_room = 0.3
        discount_apart = 0.1
    elif overnight_stays > 7:
        discount_room = 0.05
elif month == "June" or month == "September":
    room_price = 75.20
    apartment_price = 68.70
    if overnight_stays > 14:
        discount_room = 0.2
        discount_apart = 0.1
elif month == "July" or month == "August":
    room_price = 76
    apartment_price = 77
    if overnight_stays > 14:
        discount_apart = 0.1

room_price_final = room_price * overnight_stays * (1 - discount_room)
apartment_price_final = apartment_price * overnight_stays * (1 - discount_apart)

# Print Output
print(f"Apartment: {apartment_price_final:.2f} lv.")
print(f"Studio: {room_price_final:.2f} lv.")
