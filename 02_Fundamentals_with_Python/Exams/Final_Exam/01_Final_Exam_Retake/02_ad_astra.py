import re

data = input()

pattern = r"(?P<sep>[#|])(?P<name>[A-Za-z\s]+)(?P=sep)" \
          r"(?P<date>\d{2}/\d{2}/\d{2})(?P=sep)(?P<calories>\d+)(?P=sep)"
result = re.finditer(pattern, data)

total_calories = 0
items = []

for res in result:
    name = res.group("name")
    date = res.group("date")
    calories = int(res.group("calories"))
    total_calories += calories
    items.append([name, date, calories])

days = total_calories // 2000
print(f"You have food to last you for: {days} days!")

for item in items:
    print(f"Item: {item[0]}, Best before: {item[1]}, Nutrition: {item[2]}")
