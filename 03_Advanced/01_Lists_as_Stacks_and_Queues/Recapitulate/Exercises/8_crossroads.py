from collections import deque

green_light_length = int(input())
free_window = int(input())

cars = deque()
total_cars_passed = 0

while True:
    command = input()

    if command == "END":
        break
    elif command == "green":
        green_light = green_light_length

        while cars and green_light > 0:
            car = cars.popleft()

            if green_light + free_window < len(car):
                character_hit = car[green_light + free_window - len(car)]
                print(f"A crash happened!\n{car} was hit at {character_hit}.")
                exit()

            total_cars_passed += 1
            green_light -= len(car)
    else:
        cars.append(command)

print(f"Everyone is safe.\n"
      f"{total_cars_passed} total cars passed the crossroads.")
