from collections import deque

green_light = int(input())
free_window = int(input())

cars = deque()
cars_passed = 0

while True:
    command = input()
    if command == "END":
        break

    if command == "green":
        time1 = green_light

        while cars and time1 > 0:
            car = cars.popleft()

            if len(car) > time1 + free_window:
                print("A crash happened!")
                print(f"{car} was hit at {car[time1 + free_window]}.")
                exit()

            time1 -= len(car)
            cars_passed += 1
    else:
        cars.append(command)

print("Everyone is safe.")
print(f"{cars_passed} total cars passed the crossroads.")
