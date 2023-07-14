# Read user input
employees = [int(x) for x in input().split()]
factor = int(input())

# Variables

# Logic
employees = list(map(lambda x: x * factor, employees))
average_happiness = sum(employees) / len(employees)
happy_employees = list(filter(lambda x: x >= average_happiness, employees))
happy_count = len(happy_employees)
total_count = len(employees)
# End of Logic

# Print Output
if happy_count < total_count / 2:
    print(f"Score: {happy_count}/{total_count}. Employees are not happy!")
else:
    print(f"Score: {happy_count}/{total_count}. Employees are happy!")
