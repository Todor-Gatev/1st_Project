from collections import deque
from datetime import datetime, timedelta

# robots_data = deque([[x.split('-')[0], int(x.split('-')[1]), 0] for x in input().split(';')])
robots_data = [[x.split('-')[0], int(x.split('-')[1]), 0] for x in input().split(';')]
line_time = datetime.strptime(input(), "%H:%M:%S")
items = deque()

while True:
    command = input()
    if command == "End":
        break

    items.append(command)

while items:
    line_time += timedelta(0, 1)
    is_waiting_item = True
    for idx in range(len(robots_data)):
        if robots_data[idx][2] == 0 and is_waiting_item:
            item = items.popleft()
            print(f"{robots_data[idx][0]} - {item} [{line_time.strftime('%H:%M:%S')}]")
            robots_data[idx][2] = robots_data[idx][1] - 1
            is_waiting_item = False
        else:
            if robots_data[idx][2] > 0:
                robots_data[idx][2] -= 1

    if is_waiting_item:
        items.rotate(-1)
