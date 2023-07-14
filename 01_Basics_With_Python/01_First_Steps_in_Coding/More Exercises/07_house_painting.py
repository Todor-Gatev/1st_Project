# Read user input
x = float(input())
y = float(input())
h = float(input())

# Parameters
green_paint_per_sqm = 1 / 3.4
red_paint_per_sqm = 1 / 4.3
door_sqm = 1.2 * 2
window_sqm = 1.5 * 1.5

# Logic
roof_sqm = 2 * (x * y) + 2 * (x * h / 2)
walls_sqm = 2 * (x * x) \
            + 2 * (x * y) \
            - door_sqm \
            - 2 * window_sqm
needed_red_paint = roof_sqm * red_paint_per_sqm
needed_green_paint = walls_sqm * green_paint_per_sqm
# End of Logic

# Print Output
print(f'{needed_green_paint:.2f}')
print(f'{needed_red_paint:.2f}')
