
deposit = float(input())
months = int(input())
interest = float(input())

income_per_year = deposit * interest / 100
income = months * income_per_year / 12
print(deposit + income)
