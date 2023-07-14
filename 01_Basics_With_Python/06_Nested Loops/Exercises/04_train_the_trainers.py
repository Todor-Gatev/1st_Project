# Read user input
judges = int(input())

# Variables
students = 0
average_grade_sum = 0

# Logic
while True:
    user_input = input()
    if user_input == 'Finish':
        break
    students += 1
    grade_sum = 0
    for i in range(judges):
        grade_sum += float(input())
    average_grade = grade_sum / judges
    print(f"{user_input} - {average_grade:.2f}.")
    average_grade_sum += average_grade
# End of Logic

# Print Output
total_average_grade = average_grade_sum / students
print(f"Student's final assessment is {total_average_grade:.2f}.")
