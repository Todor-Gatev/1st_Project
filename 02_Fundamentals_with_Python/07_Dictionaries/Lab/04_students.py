data = input()

courses = {}

while ':' in data:
    name, id_num, course = data.split(':')

    if course not in courses:
        courses[course] = {id_num: name}
    else:
        courses[course][id_num] = name

    data = input()

# course_name = ' '.join(data.split('_'))
course_name = data.replace('_', ' ')

for key, value in courses[course_name].items():
    print(f"{value} - {key}")
