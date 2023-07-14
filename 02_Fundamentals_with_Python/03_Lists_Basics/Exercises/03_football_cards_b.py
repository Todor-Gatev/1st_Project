# Read user input
cards = input().split()

a_team_players = 11
b_team_players = 11
players_out = []

is_terminated = False

# Logic
for el in cards:
    if el in players_out:
        continue

    players_out.append(el)

    if el[0] == 'A':
        a_team_players -= 1
    elif el[0] == 'B':
        b_team_players -= 1

    if a_team_players < 7 or b_team_players < 7:
        is_terminated = True
        break
# End of Logic

# Print Output
print(f"Team A - {a_team_players}; Team B - {b_team_players}")

if is_terminated:
    print("Game was terminated")
