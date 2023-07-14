# Read user input
days = int(input())
plunder_a_day = int(input())
target = float(input())

# Variables
total_plunder = 0

# Logic
for i in range(1, days + 1):
    total_plunder += plunder_a_day
    if i % 3 == 0:
        total_plunder += plunder_a_day * 0.5
    if i % 5 == 0:
        total_plunder *= 0.7
# End of Logic

# Print Output
if total_plunder >= target:
    print(f"Ahoy! {total_plunder:.2f} plunder gained.")
else:
    percentage = (total_plunder / target) * 100
    print(f"Collected only {percentage:.2f}% of the plunder.")
