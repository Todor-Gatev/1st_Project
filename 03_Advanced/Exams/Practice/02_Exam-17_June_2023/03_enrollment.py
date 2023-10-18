def gather_credits(needed_credits: int, *args):
    courses = []
    gathered_credits = 0

    def get_result():
        return (f"Enrollment finished! Maximum credits: {gathered_credits}.\n"
                f"Courses: {', '.join(courses)}")

    if not needed_credits:
        return get_result()

    for el in args:
        if el[0] not in courses:
            gathered_credits += el[1]
            courses.append(el[0])

            if gathered_credits >= needed_credits:
                courses.sort()
                return get_result()

    return (f"You need to enroll in more courses! "
            f"You have to gather {needed_credits - gathered_credits} credits more.")


# print(gather_credits(
#     80,
#     ("Basics", 27),
# ))

# print(gather_credits(
#     60,
#     ("Basics", 27),
#     ("Fundamentals", 27),
#     ("Advanced", 30),
#     ("Web", 30)
# ))

# print(gather_credits(
#     0,
#     ("Basics", 27),
# ))
