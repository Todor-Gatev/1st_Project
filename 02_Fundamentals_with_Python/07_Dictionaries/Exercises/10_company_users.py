data = input()

companies = {}

while data != "End":
    company_name, employee_id = data.split(" -> ")

    if company_name not in companies:
        companies[company_name] = []

    if employee_id not in companies[company_name]:
        companies[company_name].append(employee_id)

    data = input()

for company_name in companies:
    print(company_name)

    for employee_id in companies[company_name]:
        print(f"-- {employee_id}")
