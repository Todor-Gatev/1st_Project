# Read user input
first_time = int(input())
second_time = int(input())
third_time = int(input())

# Logic
total_time = first_time + second_time + third_time
minutes = total_time // 60
seconds = total_time % 60
if seconds <= 9:
    print(f"{minutes}:0{seconds}")
    str_sec = "000" + str(seconds)
    print(f"{minutes}:{str_sec}")
else:
    print(f"{minutes}:{seconds}")


# a = 5
# is_positive = a > 0   # Boolean variable
# print(is_positive)    # True
