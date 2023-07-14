# Read user input
rows = int(input())

"""
4
######
##  k#
## ###
## ###
Kate got out in 5 moves
"""
# Variables
maze = []
up_bocked = False
down_bocked = False
lef_bocked = False
right_bocked = False

# Logic
for idx in range(rows):
    # row = input()
    maze.append(input())
    # row = input().replace('#', 'x')
    # print(row)
    # # if ('k' or ' ') not in row:
    # if ' ' not in row:
    #     print('b')

# End of Logic

# Print Output
print(maze)
