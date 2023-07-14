# Read user input
teams = int(input())

# Logic

mus_climbers = 0
mont_blanc_climbers = 0
kilimanjaro_climbers = 0
k_two_climbers = 0
everest_climbers = 0

for _ in range(teams):
    climbers = int(input())
    if climbers < 6:
        mus_climbers += climbers
    elif climbers < 13:
        mont_blanc_climbers += climbers
    elif climbers < 26:
        kilimanjaro_climbers += climbers
    elif climbers < 41:
        k_two_climbers += climbers
    else:
        everest_climbers += climbers

total_climbers = mus_climbers + mont_blanc_climbers \
                 + kilimanjaro_climbers + k_two_climbers + everest_climbers

# Print Output
print(f'{mus_climbers / total_climbers * 100:.2f}%')
print(f'{mont_blanc_climbers / total_climbers * 100:.2f}%')
print(f'{kilimanjaro_climbers / total_climbers * 100:.2f}%')
print(f'{k_two_climbers / total_climbers * 100:.2f}%')
print(f'{everest_climbers / total_climbers * 100:.2f}%')
