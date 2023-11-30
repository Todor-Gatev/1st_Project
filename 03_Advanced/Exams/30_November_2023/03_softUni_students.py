def softuni_students(*args, **kwargs):
    valid_courses = {}
    invalid_courses = []

    for student in args:
        id_num, name, = student[0], student[1]

        if id_num in kwargs:
            valid_courses[name] = kwargs[id_num]
        else:
            invalid_courses.append(name)

    valid_courses = sorted(valid_courses.items(), key=lambda x: x[0])
    invalid_courses.sort()

    res = [f"*** A student with the username {username} has successfully finished the course {course_name}!"
           for username, course_name in valid_courses]
    res.append(f"!!! Invalid course students: {', '.join(invalid_courses)}") if invalid_courses else None

    return "\n".join(res)


# print(softuni_students(
#     ('id_1', 'Kaloyan9905'),
#     id_1='Python Web Framework',
# ))
#
# print(softuni_students(
#     ('id_7', 'Silvester1'),
#     ('id_32', 'Katq21'),
#     ('id_7', 'The programmer'),
#     id_76='Spring Fundamentals',
#     id_7='Spring Advanced',
# ))
#
print(softuni_students(
    ('id_22', 'Programmingkitten'),
    ('id_11', 'MitkoTheDark'),
    ('id_321', 'Bobosa253'),
    ('id_08', 'KrasimirAtanasov'),
    ('id_32', 'DaniBG'),
    id_321='HTML & CSS',
    id_22='Machine Learning',
    id_08='JS Advanced',
))
