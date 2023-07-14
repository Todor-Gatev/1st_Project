from math import floor

# Read user input
tournament_num = int(input())
initial_points = int(input())

total_points = initial_points
this_year_points = 0
tournament_winner = 0

# Logic
for _ in range(tournament_num):
    stage = input()
    if stage == 'W':
        total_points += 2000
        this_year_points += 2000
        tournament_winner += 1
    elif stage == 'F':
        total_points += 1200
        this_year_points += 1200
    elif stage == 'SF':
        total_points += 720
        this_year_points += 720

average_points_per_tour = this_year_points / tournament_num
tournament_winner_percent = tournament_winner / tournament_num * 100

# Print Output
print(f'Final points: {total_points}')
print(f'Average points: {floor(average_points_per_tour)}')
print(f'{tournament_winner_percent:.2f}%')

