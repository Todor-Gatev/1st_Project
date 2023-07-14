# Read user input
bad_appraisals_allowed = int(input())

# Logic
# problem_name = ''
bad_appraisal_counter = 0
problem_counter = 0
average_score = 0
last_problem_name = ''
appraisal_sum = 0

while True:
    problem_name = input()

    if problem_name == 'Enough':
        print(f'Average score: {average_score:.2f}')
        print(f'Number of problems: {problem_counter}')
        print(f'Last problem: {last_problem_name}')
        break

    appraisal = int(input())

    if appraisal <= 4:
        bad_appraisal_counter += 1

    if bad_appraisal_counter == bad_appraisals_allowed:
        print(f'You need a break, {bad_appraisal_counter} poor grades.')
        break

    appraisal_sum += appraisal
    last_problem_name = problem_name
    problem_counter += 1
    average_score = appraisal_sum / problem_counter

# Print Output
