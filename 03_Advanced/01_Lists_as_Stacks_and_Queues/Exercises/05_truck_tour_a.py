from collections import deque

pump_info = deque()
idx_pump = 0

for _ in range(int(input())):
    data = input().split()
    litters = int(data[0])
    kilometers = int(data[1])
    pump_info.append([litters, kilometers])

while True:
    temp_pump_info = pump_info.copy()
    n = 0
    litters = 0
    while temp_pump_info:
        n += 1
        data = temp_pump_info.popleft()
        litters += data[0]
        kilometers = data[1]

        if kilometers > litters:
            pump_info.rotate(-n)
            idx_pump += n
            break

        litters -= kilometers
    else:
        break
print(idx_pump)
