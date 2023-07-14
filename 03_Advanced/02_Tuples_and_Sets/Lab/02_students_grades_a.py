from statistics import mean
from collections import defaultdict

student_info = defaultdict(list)

for _ in range(int(input())):
    name, grade = input().split()

    # if name not in student_info:
    #     student_info[name] = []

    student_info[name].append(float(grade))

for name, grades in student_info.items():
    avg = mean(grades)
    # print(f"{name} -> ", end='')
    # print(*grades, end=' ')
    # print(f"(avg: {avg:.2f})")
    print(f"{name} -> {' '.join(f'{x:.2f}' for x in grades)} (avg: {avg:.2f})")
