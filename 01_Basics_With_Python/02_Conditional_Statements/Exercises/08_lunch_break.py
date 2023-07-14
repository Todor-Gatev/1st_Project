from math import ceil

# Read user input
tv_series_name = input()
tv_series_duration = int(input())
break_duration = int(input())

lunch_duration = break_duration / 8
recreation_duration = break_duration / 4
needed_duration = tv_series_duration + lunch_duration + recreation_duration

# Logic
diff = abs(break_duration - needed_duration)
rounded = ceil(diff)

# Print Output
if break_duration >= needed_duration:
    print(f"You have enough time to watch {tv_series_name} and "
          f"left with {rounded} minutes free time.")
else:
    print(f"You don't have enough time to watch {tv_series_name}, "
          f"you need {rounded} more minutes.")
