
square_meters = float(input())
cost_per_sqm = 7.61
grand_cost = square_meters * cost_per_sqm
discount = grand_cost * 0.18
print(f"The final price is: {grand_cost - discount} lv.")
print(f"The discount is: {discount} lv.")
