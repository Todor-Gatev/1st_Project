# Read user input
open_tab_num = int(input())
salary = int(input())

total_fines = 0
final_salary = 0

# Logic
for _ in range(open_tab_num):
    tab_name = input()
    if tab_name == "Facebook":
        total_fines += 150
    elif tab_name == "Instagram":
        total_fines += 100
    elif tab_name == "Reddit":
        total_fines += 50
    final_salary = salary - total_fines
    if final_salary <= 0:
        print("You have lost your salary.")
        break
else:
    print(final_salary)
