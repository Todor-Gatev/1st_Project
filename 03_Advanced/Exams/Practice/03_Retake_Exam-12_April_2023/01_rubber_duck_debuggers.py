from collections import deque

needed_times = deque(int(x) for x in input().split())
tasks = [int(x) for x in input().split()]
ducks = {
    "Darth Vader Ducky": 0,
    "Thor Ducky": 0,
    "Big Blue Rubber Ducky": 0,
    "Small Yellow Rubber Ducky": 0,
}

while tasks:
    needed_time = needed_times.popleft()
    task = tasks.pop()

    multiply = needed_time * task

    if multiply < 61:
        ducks["Darth Vader Ducky"] += 1
    elif multiply < 121:
        ducks["Thor Ducky"] += 1
    elif multiply < 181:
        ducks["Big Blue Rubber Ducky"] += 1
    elif multiply < 241:
        ducks["Small Yellow Rubber Ducky"] += 1
    else:
        needed_times.append(needed_time)
        tasks.append(task - 2)

print("Congratulations, all tasks have been completed! Rubber ducks rewarded:")

[print(f"{duck}: {ducks[duck]}") for duck in ducks]
