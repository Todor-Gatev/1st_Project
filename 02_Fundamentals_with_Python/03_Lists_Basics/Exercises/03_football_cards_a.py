# Read user input
cards = input().split()

# Variables
a_team_players_with_card = []
b_team_players_with_card = []
a_team_players_left = 11
b_team_players_left = 11
is_game_terminated = False

# Logic
for el in cards:
    if el[0] == 'A':
        if el not in a_team_players_with_card:
            a_team_players_with_card.append(el)
    else:
        if el not in b_team_players_with_card:
            b_team_players_with_card.append(el)

    a_team_players_left = 11 - len(a_team_players_with_card)
    b_team_players_left = 11 - len(b_team_players_with_card)

    if a_team_players_left < 7 or b_team_players_left < 7:
        is_game_terminated = True
        break
# End of Logic

# Print Output
print(f"Team A - {a_team_players_left}; "
      f"Team B - {b_team_players_left}")

if is_game_terminated:
    print("Game was terminated")
