# Read user input
projection = input()
rows = int(input())
columns = int(input())

# Logic
price = 0
if projection == "Premiere":  #
    price = 12.00
elif projection == "Normal":  #
    price = 7.50
elif projection == "Discount":  #
    price = 5.00

# Print Output
seats_number = rows * columns
income = price * seats_number
print(f'{income:.2f}')
