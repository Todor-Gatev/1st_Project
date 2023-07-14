# Read user input

# Logic
steps_target = 10000
gabi_input = ''
total_steps = 0
current_steps = 0

while steps_target >= total_steps:
    gabi_input = input()

    if gabi_input == "Going home":
        current_steps = int(input())
        total_steps += current_steps
        break
    else:
        current_steps = int(gabi_input)
        total_steps += current_steps
    #
    # if total_steps >= steps_target:
    #     break

diff = abs(total_steps - steps_target)

# Print Output
if total_steps >= steps_target:
    print(f'Goal reached! Good job!')
    print(f"{diff} steps over the goal!")
else:
    print(f"{diff} more steps to reach goal.")
