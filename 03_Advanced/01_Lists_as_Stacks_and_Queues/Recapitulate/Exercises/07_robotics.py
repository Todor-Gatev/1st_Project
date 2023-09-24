from collections import deque
# import time


data = input().split(';')
input_time = int(input())
process_time = int(input())

details = deque()
robots = []
is_new_detail = True

for el in data:
    name, processing_time = el.split('-')
    robots.append([name, int(processing_time), 0])

while True:
    if is_new_detail:
        command = input()

        if command == "End":
            is_new_detail = False
        else:
            details.appendleft(command)

    is_detail_in_processing = False
    process_time += 1

    for robot in robots:
        if is_detail_in_processing:
            if robot[2] == 0:
                continue

            robot[2] += 1
        else:
            if robot[2] == 0:
                is_detail_in_processing = True
                print(f"{robot[0]} - {details.popleft()} [{process_time}]")

            robot[2] += 1

        if robot[2] == robot[1]:
            robot[2] = 0

    if not is_detail_in_processing:
        details.rotate(-1)
    elif not details and not is_new_detail:
        break

# NX8000 - apple [08:00:06]

# ROB-15;SS2-10;NX8000-3
# 8:00:00
# detail
# glass
# wood
# apple
# End
