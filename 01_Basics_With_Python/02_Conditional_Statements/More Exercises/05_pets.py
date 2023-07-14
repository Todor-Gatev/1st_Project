from math import ceil

# Read user input
days_number = int(input())
food_kg = int(input())
dog_food_per_day = float(input())               # in kg
cat_food_per_day = float(input())               # in kg
turtle_food_per_day = float(input()) / 1000     # in gr -> gr to kg

# Parameters
needed_food = days_number * (dog_food_per_day + cat_food_per_day + turtle_food_per_day)
diff_food = food_kg - needed_food

# Logic
if food_kg >= needed_food:
    print(f"{int(diff_food)} kilos of food left.")
else:
    print(f'{ceil(-diff_food)} more kilos of food are needed.')

# End of Logic

# Print Output
