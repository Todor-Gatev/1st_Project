from math import ceil

# Read user input
height = int(input())
width = int(input())
doors_windows_percent = int(input())

# Parameters
doors_windows = 4 * height * width * doors_windows_percent / 100
# doors_windows_int = int(doors_windows)
area_for_painting = (4 * height * width) - doors_windows
litters = 0

# Logic
while area_for_painting > 0:
    user_input = input()

    if user_input == 'Tired!':
        print(f'{ceil(area_for_painting)} quadratic m left.')
        break
    else:
        litters = int(user_input)
        area_for_painting -= litters
else:
    if area_for_painting < 0:
        diff = -ceil(area_for_painting)
        print(f"All walls are painted and you have "
              f"{diff} l paint left!")
    else:
        print("All walls are painted! Great job, Pesho!")
# End of Logic
