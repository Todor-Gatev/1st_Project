# Read user input
number_of_rooms = int(input())

# Variables
total_free_chairs = 0
is_game_on = True

# Logic
for number_of_room in range(1, number_of_rooms + 1):
    room_info = input().split()
    chairs = len(room_info[0])
    visitors = int(room_info[1])
    if visitors > chairs:
        needed_chairs_in_room = visitors - chairs
        print(f"{needed_chairs_in_room} more chairs needed in room {number_of_room}")
        is_game_on = False
    else:
        total_free_chairs += chairs - visitors

# End of Logic

# Print Output
if is_game_on:
    print(f"Game On, {total_free_chairs} free chairs left")
