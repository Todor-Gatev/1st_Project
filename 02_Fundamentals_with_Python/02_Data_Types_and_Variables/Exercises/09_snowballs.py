# Read user input
snowballs = int(input())

# Variables
# highest_value_snowball = 0
snowball_value = 0
snowball_weight = 0
snowball_time = 0
snowball_quality = 0

# Logic
for _ in range(snowballs):
    weight = int(input())
    time = int(input())
    quality = int(input())

    value = (weight / time) ** quality

    if value > snowball_value:
        snowball_value = value
        snowball_weight = weight
        snowball_time = time
        snowball_quality = quality

# End of Logic

# Print Output
print(f"{snowball_weight} : {snowball_time} = {int(snowball_value)} ({snowball_quality})")
