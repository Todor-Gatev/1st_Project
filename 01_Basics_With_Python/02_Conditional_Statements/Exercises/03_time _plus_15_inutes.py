# Read user input
hours = int(input())
minutes = int(input())

new_hours = 0
new_minutes = 0

# Logic
if minutes + 15 < 60:
    new_hours = hours
    new_minutes = minutes + 15
else:
    new_hours = hours + 1
    new_minutes = minutes + 15 - 60

if new_hours == 24:
    new_hours = 0

# Print Output
if new_minutes < 10:
    print(f"{new_hours}:0{new_minutes}")
else:
    print(f"{new_hours}:{new_minutes}")
