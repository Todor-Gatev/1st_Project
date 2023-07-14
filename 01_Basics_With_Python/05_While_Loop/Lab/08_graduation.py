# Read user input
student_name = input()

# Logic

# average_grade = 0
# year_counter = 0
average_grade_counter = 0
year_evaluation = 0
fail_counter = 0
evaluation_sum = 0
total_years = 13

for year in range(1, total_years):
    year_evaluation = float(input())
    if year_evaluation < 4:
        fail_counter += 1
        year -= 1
        total_years += 1
        if fail_counter == 2:
            print(f'{student_name} has been excluded at {year} grade')
            break
    else:
        evaluation_sum += year_evaluation
        average_grade_counter += 1
else:
    average_grade = evaluation_sum / 12
    print(f'{student_name} graduated. Average grade: {average_grade:.2f}')
    print(average_grade_counter)

# Print Output
