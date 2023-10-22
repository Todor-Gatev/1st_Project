def team_lineup(*args):
    teams = {}

    for info in args:
        if info[1] not in teams:
            teams[info[1]] = []

        teams[info[1]].append(info[0])

    sorted_teams = sorted(teams.items(), key=lambda x: (-len(x[1]), x[0],))
    result = []
    for t, ps in sorted_teams:
        result.append(f"{t}:")
        result.extend(f"  -{p}" for p in ps)

    return "\n".join(result)


print(team_lineup(
   ("Harry Kane", "England"),
   ("Manuel Neuer", "Germany"),
   ("Raheem Sterling", "England"),
   ("Toni Kroos", "Germany"),
   ("Cristiano Ronaldo", "Portugal"),
   ("Thomas Muller", "Germany")))
