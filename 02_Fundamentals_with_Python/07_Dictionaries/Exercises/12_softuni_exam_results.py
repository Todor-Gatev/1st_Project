def get_input():
    return input()


data = get_input()

results = {}
submissions = {}
banned = []

while data != "exam finished":
    data = data.split('-')
    if len(data) < 3:
        username = data[0]
        banned.append(username)

        if username in results:
            results.pop(username)

        data = get_input()
        continue

    username, language, points = data
    points = int(points)

    if language not in submissions:
        submissions[language] = 0

    submissions[language] += 1

    if username in banned:
        data = get_input()
        continue

    if username not in results:
        results[username] = {}

    if language not in results[username]:
        results[username][language] = points
    else:
        if points > results[username][language]:
            results[username][language] = points

    data = get_input()

if results:
    print("Results:")
    for username in results:
        for language, points in results[username].items():
            print(f"{username} | {points}")

if submissions:
    print("Submissions:")
    for language, submissions_count in submissions.items():
        print(f"{language} - {submissions_count}")
