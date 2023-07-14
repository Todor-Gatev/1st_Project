# Read user input
side_a = float(input())
height = float(input())

# Logic
area = side_a * height / 2

# End of Logic

# Print Output
print(f'{area:.2f}')
# area_test = {area: .2f}  -> not working
area_test = f'{area: .2f}'
print(area_test)
