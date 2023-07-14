# Read user input
initial_score = int(input())

bonus = 0
add_points = 0

# Logic
if initial_score <= 100:
    bonus = 5
elif initial_score <= 1000:
    bonus = initial_score * 0.2
else:
    bonus = initial_score * 0.1

if initial_score % 2 == 0:
    add_points = 1
elif initial_score % 5 == 0:
    add_points = 2

# Print Output
print(add_points + bonus)
print(initial_score + add_points + bonus)
