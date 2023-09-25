from collections import deque
from datetime import datetime, timedelta

# robots1 = {x.split("-")[0]: [int(x.split("-")[1]), 0] for x in input().split(';')}
robots = {}
details = deque()
is_command_pending = True

for el in input().split(';'):
    name, processing_time = el.split('-')
    robots[name] = [int(processing_time), 0]

current_time = datetime.strptime(input(), "%H:%M:%S")

while True:
    if is_command_pending:
        command = input()

        if command == "End":
            is_command_pending = False
        else:
            details.appendleft(command)

    if not details:
        break

    is_robot_needed = True
    current_time += timedelta(seconds=1)
# class datetime.timedelta(days=0, seconds=0, microseconds=0, milliseconds=0, minutes=0, hours=0, weeks=0)
    for name in robots:
        if is_robot_needed and robots[name][1] == 0:
            is_robot_needed = False
            robots[name][1] = robots[name][0] - 1
            print(f"{name} - {details.popleft()} {current_time.strftime('[%H:%M:%S]')}")
        elif robots[name][1] > 0:
            robots[name][1] -= 1

    if is_robot_needed:
        details.rotate(-1)
