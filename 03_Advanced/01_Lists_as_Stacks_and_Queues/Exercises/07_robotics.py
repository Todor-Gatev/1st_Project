from collections import deque


def line_time(h, m, s):
    s += 1
    if s == 60:
        s = 0
        m += 1
        if m == 60:
            m = 0
            h += 1
            if h == 24:
                h = 0
    return h, m, s


details = deque()
robots = {}

for robot in input().split(';'):
    robot_name, robot_time = robot.split('-')
    robots[robot_name] = [int(robot_time), 0]

hh, mm, ss = [int(x) for x in input().split(':')]


while True:
    data = input()
    if data == "End":
        break

    details.append(data)

while details:
    hh, mm, ss = line_time(hh, mm, ss)
    time = f"[{hh:02d}:{mm:02d}:{ss:02d}]"
    is_free_robot_needed = True

    for robot in robots:
        if robots[robot][1] == 0 and is_free_robot_needed:
            robots[robot][1] = robots[robot][0] - 1
            detail = details.popleft()
            print(f"{robot} - {detail} {time}")
            is_free_robot_needed = False
        else:
            if robots[robot][1] != 0:
                robots[robot][1] -= 1

    if is_free_robot_needed:
        details.rotate(-1)
