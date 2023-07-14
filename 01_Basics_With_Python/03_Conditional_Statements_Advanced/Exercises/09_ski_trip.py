# Read user input
days_num = int(input())
room_type = input()
rating = input()

# Logic
price_per_night = 0
discount = 0
price = 0

if room_type == "room for one person":
    price_per_night = 18
elif room_type == "apartment":
    price_per_night = 25
elif room_type == "president apartment":
    price_per_night = 35

if days_num - 1 < 10:
    if room_type == "apartment":
        discount = 0.3
    if room_type == "president apartment":
        discount = 0.1
elif 0 <= days_num - 1 <= 15:
    if room_type == "apartment":
        discount = 0.35
    if room_type == "president apartment":
        discount = 0.15
else:
    if room_type == "apartment":
        discount = 0.50
    if room_type == "president apartment":
        discount = 0.20

if rating == "positive":
    price = price_per_night * (days_num - 1) * (1 - discount) * 1.25
elif rating == "negative":
    price = price_per_night * (days_num - 1) * (1 - discount) * 0.9

# Print Output
print(f"{price:.2f}")
