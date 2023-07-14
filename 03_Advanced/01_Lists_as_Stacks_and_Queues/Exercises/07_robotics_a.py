from collections import deque
from datetime import datetime, timedelta

details = deque()
robots = {}

for robot in input().split(';'):
    robot_name, robot_time = robot.split('-')
    robots[robot_name] = [int(robot_time), 0]

line_time = datetime.strptime(input(), "%H:%M:%S")

while True:
    detail = input()
    if detail == "End":
        break

    details.append(detail)

while details:
    line_time += timedelta(0, 1)
    is_free_robot_needed = True

    for robot in robots:
        if robots[robot][1] == 0 and is_free_robot_needed:
            robots[robot][1] = robots[robot][0] - 1
            detail = details.popleft()
            print(f"{robot} - {detail} {line_time.strftime('[%H:%M:%S]')}")
            is_free_robot_needed = False
        else:
            if robots[robot][1] != 0:
                robots[robot][1] -= 1

    if is_free_robot_needed:
        details.rotate(-1)
