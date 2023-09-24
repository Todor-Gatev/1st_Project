from collections import deque

n = int(input())

petrol_stations = deque()

for i in range(n):
    litters, km = [int(x) for x in input().split()]
    petrol_stations.append([i, litters, km])

while True:
    litters_in_tank = 0

    for i in range(n):
        litters_in_tank += petrol_stations[i][1]
        if petrol_stations[i][2] > litters_in_tank:
            petrol_stations.rotate(-1)
            break

        litters_in_tank -= petrol_stations[i][2]
    else:
        break

print(petrol_stations[0][0])
