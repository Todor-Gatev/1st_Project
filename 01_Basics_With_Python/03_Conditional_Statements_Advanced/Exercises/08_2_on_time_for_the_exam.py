# Read user input
exam_hour = int(input())
exam_minutes = int(input())
arrival_hour = int(input())
arrival_minutes = int(input())

# Logic
exam_time_in_minutes = exam_hour * 60 + exam_minutes
arrival_time_in_minutes = arrival_hour * 60 + arrival_minutes

diff_time = abs(exam_time_in_minutes - arrival_time_in_minutes)
diff_hours = 0
diff_minutes = 0
is_valid = True

if diff_time > 59:
    is_valid = False
    diff_hours = diff_time // 60
    diff_minutes = diff_time % 60

if exam_time_in_minutes < arrival_time_in_minutes:
    print("Late")
    if is_valid:
        print(f"{diff_time} minutes after the start")
    else:
        print(f"{diff_hours}:{diff_minutes:02d} hours after the start")
elif diff_time <= 30:
    print("On time")
    if diff_time > 0:
        print(f"{diff_time} minutes before the start")
else:
    print("Early")
    if is_valid:
        print(f"{diff_time} minutes before the start")
    else:
        print(f"{diff_hours}:{diff_minutes:02d} hours before the start")

# Print Output
