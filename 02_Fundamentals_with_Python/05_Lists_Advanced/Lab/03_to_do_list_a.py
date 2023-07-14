# Read user input
command = input()

# Variables
to_do_notes = [0] * 10

# Logic
while command != "End":
    importance, task = command.split('-')
    index = int(importance) - 1
    to_do_notes.pop(index)
    to_do_notes.insert(index, task)
    # to_do_notes[index] = task
    command = input()
# End of Logic

# Print Output
print([x for x in to_do_notes if x != 0])
