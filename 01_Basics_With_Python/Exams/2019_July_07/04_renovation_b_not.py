from math import ceil

# Read user input
height = int(input())
width = int(input())
doors_windows_percent = int(input())

# Parameters
doors_windows = 4 * height * width * doors_windows_percent / 100
# doors_windows_int = int(doors_windows)
doors_windows_int = ceil(doors_windows)
area_for_painting = (4 * height * width) - doors_windows_int

# Logic
while area_for_painting > 0:
    user_input = input()

    if user_input == 'Tired!':
        print(f'{area_for_painting} quadratic m left.')
        break
    else:
        area_for_painting -= int(user_input)
else:
    if area_for_painting < 0:
        print(f"All walls are painted and you have "
              f"{- area_for_painting} l paint left!")
    else:
        print("All walls are painted! Great job, Pesho!")
# End of Logic
