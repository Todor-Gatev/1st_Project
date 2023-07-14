from math import ceil

# Read user input
students = int(input())
lectures = int(input())
bonus = int(input())

# Variables
max_bonus_points = 0
student_attendances = 0

# Logic
for _ in range(students):
    attendances = int(input())
    total_bonus = attendances / lectures * (5 + bonus)

    if total_bonus > max_bonus_points:
        max_bonus_points = total_bonus
        student_attendances = attendances
# End of Logic

# Print Output
print(f"Max Bonus: {ceil(max_bonus_points)}.")
print(f"The student has attended {student_attendances} lectures.")

