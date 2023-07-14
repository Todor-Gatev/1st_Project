# Read user input
student_name = input()

# Logic
# annual_evaluation = 0
# average_grade = 0
year_counter = 0
failed_year = 0
evaluation_sum = 0

while True:
    annual_evaluation = float(input())
    year_counter += 1
    if annual_evaluation < 4:
        failed_year += 1
        if failed_year == 2:
            print(f'{student_name} has been excluded at {year_counter} grade')
            break
        year_counter -= 1
    else:
        evaluation_sum += annual_evaluation

    if year_counter == 12:
        average_grade = evaluation_sum / 12
        print(f'{student_name} graduated. Average grade: {average_grade:.2f}')
        break
