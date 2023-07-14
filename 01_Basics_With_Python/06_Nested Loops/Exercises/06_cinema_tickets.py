# Variables
total_students = 0
total_standard = 0
total_kids = 0

# Logic
while True:
    user_input = input()
    if user_input == 'Finish':
        break

    places_available = int(input())
    free_places = places_available
    students = 0
    standard = 0
    kids = 0

    while True:
        if free_places <= 0:
            break

        ticket_type = input()

        if ticket_type == 'End':
            break
        elif ticket_type == 'student':
            students += 1
        elif ticket_type == 'standard':
            standard += 1
        elif ticket_type == 'kid':
            kids += 1

        free_places -= 1
    percent_full = (students + standard + kids) * 100 / places_available
    print(f"{user_input} - {percent_full:.2f}% full.")

    total_students += students
    total_standard += standard
    total_kids += kids
# End of Logic

# Print Output
total_tickets = total_students + total_standard + total_kids
percent_students = total_students / total_tickets * 100
percent_standard = total_standard / total_tickets * 100
percent_kids = total_kids / total_tickets * 100
print(f'Total tickets: {total_tickets}')
print(f"{percent_students:.2f}% student tickets.")
print(f"{percent_standard:.2f}% standard tickets.")
print(f"{percent_kids:.2f}% kids tickets.")
