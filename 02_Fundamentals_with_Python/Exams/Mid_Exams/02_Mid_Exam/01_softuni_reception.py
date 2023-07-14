# Read user input
first = int(input())
second = int(input())
third = int(input())

students = int(input())

# Variables
hours = 0
answers_per_hour = first + second + third

# Logic
while students > 0:
    hours += 1
    if hours % 4 == 0:
        continue

    students -= answers_per_hour
# End of Logic

# Print Output
print(f"Time needed: {hours}h.")
