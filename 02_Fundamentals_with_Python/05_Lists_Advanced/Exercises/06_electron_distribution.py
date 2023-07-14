# Read user input
electrons = int(input())

# Variables
filled_shells = []
shell = 1

# Logic
while electrons > 0:
    needed_electrons = 2 * (shell ** 2)
    filled_shells.append(min(needed_electrons, electrons))
    # if needed_electrons <= electrons:
    #     filled_shells.append(needed_electrons)
    #     # filled_shells.insert(shell-1, needed_electrons)
    # else:
    #     filled_shells.append(electrons)
    #     # filled_shells.insert(shell-1, electrons)

    electrons -= needed_electrons
    shell += 1
# End of Logic

# Print Output
print(filled_shells)
