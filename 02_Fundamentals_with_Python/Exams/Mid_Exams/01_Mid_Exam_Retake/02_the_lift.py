# Read user input
people = int(input())
current_state = [int(x) for x in input().split()]
new_state = []

# Variables

# Logic
for num in current_state:
    free_places = 4 - num

    if people >= free_places:
        people -= free_places
        new_state.append(4)
    else:
        new_state.append(num + people)
        people = 0
# End of Logic

# Print Output
if people == 0 and min(new_state) < 4:
    print("The lift has empty spots!")
    [print(x, end=' ') for x in new_state]
elif people > 0:
    print(f"There isn't enough space! {people} people in a queue!")
    [print(x, end=' ') for x in new_state]
else:
    [print(x, end=' ') for x in new_state]
