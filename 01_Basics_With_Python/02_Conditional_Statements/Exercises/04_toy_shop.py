# Read user input
trip_price = float(input())
puzzle_pcs = int(input())
doll_pcs = int(input())
bear_pcs = int(input())
minion_pcs = int(input())
truck_pcs = int(input())

# Logic
puzzle_income = puzzle_pcs * 2.60
doll_income = doll_pcs * 3
bear_income = bear_pcs * 4.10
minion_income = minion_pcs * 8.20
truck_income = truck_pcs * 2

cost = puzzle_income + doll_income + bear_income + \
       minion_income + truck_income

total_pcs = puzzle_pcs + doll_pcs + bear_pcs + \
            minion_pcs + truck_pcs

discount = 0
if total_pcs >= 50:
    discount = cost * 0.25

income = cost - discount

profit = income * 0.9
#
# Print Output
if profit < trip_price:
    print(f"Not enough money! {trip_price - profit:.2f} lv needed.")
else:
    print(f"Yes! {profit - trip_price:.2f} lv left.")
