# Read user input
schedule = input().split(", ")
command = input()

# Variables
exercises = []

# Logic
while command != "course start":
    info = command.split(':')
    action, lesson = info[0], info[1]

    if action == "Add":
        if lesson not in schedule:
            schedule.append(lesson)
    elif action == "Insert":
        if lesson not in schedule:
            index = int(info[2])
            schedule.insert(index, lesson)
    elif action == "Remove":
        if lesson in schedule:
            schedule.remove(lesson)

        if lesson in exercises:
            exercises.remove(lesson)
    elif action == "Swap":
        lesson2 = info[2]
        if (lesson and lesson2) in schedule:
            lesson_idx = schedule.index(lesson)
            lesson2_idx = schedule.index(lesson2)
            schedule[lesson_idx], schedule[lesson2_idx] = schedule[lesson2_idx], schedule[lesson_idx]
    elif action == "Exercise":
        if lesson not in schedule:
            schedule.append(lesson)

        if lesson not in exercises:
            exercises.append(lesson)
    command = input()
# End of Logic

# Print Output
idx = 1
for lesson in schedule:
    print(f"{idx}.{lesson}")
    idx += 1

    if lesson in exercises:
        print(f"{idx}.{lesson}-Exercise")
        idx += 1
