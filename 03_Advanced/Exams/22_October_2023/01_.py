from collections import deque

fuel = [int(x) for x in input().split()]
additional_fuel = deque(int(x) for x in input().split())
needed_fuel = deque(int(x) for x in input().split())

reached_altitude = 1

while needed_fuel:
    total = fuel.pop() - additional_fuel.popleft()
    n = needed_fuel.popleft()

    if total < n:
        print(f"John did not reach: Altitude {reached_altitude}")
        needed_fuel.append(n)
        break

    print(f"John has reached: Altitude {reached_altitude}")
    reached_altitude += 1

if needed_fuel:
    print("John failed to reach the top.")
    if reached_altitude > 1:
        reached = [f"Altitude {i}" for i in range(1, reached_altitude)]
        print(f"Reached altitudes: {', '.join(reached)}")
    else:
        print("John didn't reach any altitude.")
else:
    print("John has reached all the altitudes and managed to reach the top!")

