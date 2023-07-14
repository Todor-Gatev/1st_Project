# Read user input
holidays = int(input())

# Parameters
needed_play_time = 30000  # minutes
working_days = 365 - holidays
real_play_time = (working_days * 63) + (holidays * 127)
# minutes_per_year = 365 * 24 * 60
# real_rest_time = minutes_per_year - play_time

diff = needed_play_time - real_play_time
diff_hours = abs(diff) // 60
diff_minutes = abs(diff) % 60

# Logic
if diff >= 0:
    print('Tom sleeps well')
    print(f'{diff_hours} hours and {diff_minutes} minutes less for play')
else:
    print('Tom will run away')
    print(f'{diff_hours} hours and {diff_minutes} minutes more for play')
# End of Logic

# Print Output
