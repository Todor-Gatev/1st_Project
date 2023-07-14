def is_lesson_exist(f_schedule, f_lesson):
    for el_f in f_schedule:
        if el_f[0] == f_lesson[0]:
            return True
    else:
        return False


def is_exercise(f_lesson):
    if len(f_lesson) == 1:
        return False
    else:
        return True


# Read user input
schedule = [[x] for x in input().split(", ")]
command = input()

# Variables

# Logic
while command != "course start":
    data = command.split(':')
    action, lesson = data[0], [data[1]]
    if action == "Add":
        if not is_lesson_exist(schedule, lesson):
            schedule.append(lesson)
    elif action == "Insert":
        if not is_lesson_exist(schedule, lesson):
            schedule.insert(int(data[2]), lesson)
    elif action == "Remove":
        if is_lesson_exist(schedule, lesson):
            schedule.remove(lesson)
    elif action == "Swap":
        if is_lesson_exist(schedule, lesson):
            lesson_two = [data[2]]
            if is_lesson_exist(schedule, lesson_two):
                index = None
                index_two = None
                for i in range(len(schedule)):
                    if (schedule[i])[0] == lesson[0]:
                        index = i
                    if (schedule[i])[0] == lesson_two[0]:
                        index_two = i
                    if index is not None and index_two is not None:
                        break

                schedule[index], schedule[index_two] = schedule[index_two], schedule[index]
    elif action == "Exercise":
        if not is_lesson_exist(schedule, lesson):
            schedule.append(lesson)

        if not is_exercise(lesson):
            exercise = f"{lesson[0]}-Exercise"
            for el in schedule:
                if el[0] == lesson[0]:
                    el.append(exercise)
                    break

    command = input()
# End of Logic

# Print Output
lesson_index = 0
for el in schedule:
    lesson_index += 1
    if is_exercise(el):
        print(f"{lesson_index}.{el[0]}")
        lesson_index += 1
        print(f"{lesson_index}.{el[1]}")
    else:
        print(f"{lesson_index}.{el[0]}")
