def students_credits(*args):
    gained_credits = 0
    finished_courses = {}
    result = []

    for el in args:
        course, possible_credits, max_points, d_points = el.split("-")
        received_credits = int(possible_credits) * (int(d_points) / int(max_points))
        # received_credits = min(received_credits, possible_credits)
        gained_credits += received_credits
        finished_courses[course] = received_credits

    if gained_credits >= 240:
        result.append(f"Diyan gets a diploma with {gained_credits:.1f} credits.")
    else:
        result.append(f"Diyan needs {240 - gained_credits:.1f} credits more for a diploma.")

    sorted_courses = sorted(finished_courses.items(), key=lambda x: -x[1])

    for name, points in sorted_courses:
        result.append(f'{name} - {points:.1f}')

    return "\n".join(result)


print(students_credits("Computer Science-12-300-300", "AComputer Science-12-300-300", "Algorithms-25-500-490"))
# print(students_credits("Computer Science-12-300-300"))

# print(
#     students_credits(
#         "Computer Science-12-300-250",
#         "Basic Algebra-15-400-200",
#         "Algorithms-25-500-490"
#     )
# )

# print(
#     students_credits(
#         "Discrete Maths-40-500-450",
#         "AI Development-20-400-400",
#         "Algorithms Advanced-50-700-630",
#         "Python Development-15-200-200",
#         "JavaScript Development-12-500-480",
#         "C++ Development-30-500-405",
#         "Game Engine Development-70-100-70",
#         "Mobile Development-25-250-225",
#         "QA-20-300-300",
#     )
# )
#
# print(
#     students_credits(
#         "Python Development-15-200-200",
#         "JavaScript Development-12-500-480",
#         "C++ Development-30-500-405",
#         "Java Development-10-300-150"
#     )
# )
