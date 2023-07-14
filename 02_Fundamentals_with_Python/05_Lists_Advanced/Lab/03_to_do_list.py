# Read user input
command = input()

# Variables
to_do_notes = ['0'] * 10

# Logic
while command != "End":
    note = command.split('-')
    index = int(note[0]) - 1
    to_do_notes[index] = note[1]
    command = input()
# End of Logic

# Print Output
print([x for x in to_do_notes if x != '0'])
