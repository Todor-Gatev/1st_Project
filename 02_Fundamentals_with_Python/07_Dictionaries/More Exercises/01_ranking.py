data = input()

contests = {}
results = {}
best_candidate = ""
max_points = 0

while data != "end of contests":
    contest, password = data.split(':')
    contests[contest] = password
    data = input()

data = input()

while data != "end of submissions":
    contest, password, username, points = data.split('=>')
    points = int(points)
    if contest in contests:
        if contests[contest] == password:
            if username not in results:
                results[username] = {contest: points}
                continue

            if contest not in results[username]:
                results[username][contest] = points
                continue

            if results[username][contest] < points:
                results[username][contest] = points

    data = input()

for user, file in results.items():
    total_user_points = 0
    for contest, points in file.items():
        total_user_points += points

    if total_user_points > max_points:
        max_points = total_user_points
        best_candidate = user

results = dict(sorted(results.items()))

print(f"Best candidate is {best_candidate} with total {max_points} points.")
print("Ranking:")

for user, file in results.items():
    print(user)
    file_sorted = dict(sorted(file.items(), key=lambda x: -x[1]))
    for contest, points in file_sorted.items():
        print(f"#  {contest} -> {points}")
