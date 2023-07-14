data = input()

courses = {}

while data != "end":
    course_name, student_name = data.split(" : ")

    if course_name not in courses:
        courses[course_name] = []

    courses[course_name].append(student_name)
    data = input()

for course_name, student_name in courses.items():
    registered_students = len(courses[course_name])
    print(f"{course_name}: {registered_students}")

    for student in courses[course_name]:
        print(f"-- {student}")
