# from math import ceil

# Read user input
height = int(input())
width = int(input())
doors_windows_percent = int(input())

# Parameters
doors_windows = 4 * height * width * doors_windows_percent / 100
doors_windows_int = int(doors_windows)
area_for_painting = (4 * height * width) - doors_windows_int

# Logic
while area_for_painting > 0:
    user_input = input()

    if user_input == 'Tired!':
        break

    area_for_painting -= int(user_input)

if area_for_painting < 0:
    print(f"All walls are painted and you have "
          f"{- area_for_painting} l paint left!")
elif area_for_painting > 0:
    print(f'{area_for_painting} quadratic m left.')
else:
    print("All walls are painted! Great job, Pesho!")
# End of Logic
