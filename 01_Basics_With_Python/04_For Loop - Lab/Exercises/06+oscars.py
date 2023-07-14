# Read user input
actor_name = input()
total_points = float(input())
jury_members_num = int(input())

# Logic

for _ in range(jury_members_num):
    appraiser_name = input()
    appraiser_name_len = len(appraiser_name)
    appraiser_points = float(input())
    total_points += appraiser_points * appraiser_name_len / 2
    if total_points > 1250.5:
        print(f'Congratulations, {actor_name} got a nominee for leading role with {total_points:.1f}!')
        break
else:
    diff = abs(total_points - 1250.5)
    print(f'Sorry, {actor_name} you need {diff:.1f} more!')
