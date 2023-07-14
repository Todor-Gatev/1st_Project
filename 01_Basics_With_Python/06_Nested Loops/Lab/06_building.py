# Read user input
floors_num = int(input())
rooms_num = int(input())

# Logic
for current_floor in range(floors_num, 0, -1):
    for current_room in range(rooms_num):
        if current_floor == floors_num:
            apartment_or_office_letter = 'L'
        elif current_floor % 2 == 0:
            apartment_or_office_letter = 'O'
        else:
            apartment_or_office_letter = 'A'
        # apartment_or_office_identifier = apartment_or_office_letter + str(current_floor) + str(current_room)
        apartment_or_office_identifier = f'{apartment_or_office_letter}' \
                                         f'{current_floor}{current_room}'
        print(apartment_or_office_identifier, end=' ')
    print()
# End of Logic
