from collections import deque

seats = input().split(", ")
first_nums = deque(int(x) for x in input().split(", "))
second_nums = deque(int(x) for x in input().split(", "))

taken_seats = []
rotations = 0

while rotations < 10 and len(taken_seats) < 3:
    rotations += 1
    first = first_nums.popleft()
    second = second_nums.pop()
    letter = chr(first + second)

    if str(first) + letter in taken_seats or str(second) + letter in taken_seats:
        continue
    elif str(first) + letter in seats:
        taken_seats.append(str(first) + letter)
    elif str(second) + letter in seats:
        taken_seats.append(str(second) + letter)
    else:
        first_nums.append(first)
        second_nums.appendleft(second)

print(f"Seat matches: {', '.join(taken_seats)}")
print(f"Rotations count: {rotations}")
