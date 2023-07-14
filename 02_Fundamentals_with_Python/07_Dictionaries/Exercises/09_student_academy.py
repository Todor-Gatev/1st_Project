n = int(input())

students = {}

for _ in range(n):
    name = input()
    grade = float(input())

    if name not in students:
        # if grade < 4.5:
        #     continue
        students[name] = []

    students[name].append(grade)
    # averageGrade = sum(students[name]) / len(students[name])
    #
    # if averageGrade < 4.5:
    #     students.pop(name)

for name in students:
    averageGrade = sum(students[name]) / len(students[name])
    if averageGrade >= 4.5:
        print(f"{name} -> {averageGrade:.2f}")
