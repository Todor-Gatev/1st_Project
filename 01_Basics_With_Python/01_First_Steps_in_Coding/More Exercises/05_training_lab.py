# Read user input
width = float(input())
height = float(input())

# Parameters
working_space_h = 0.7
working_space_w = 1.2
working_space = working_space_w * working_space_h
min_corridor_height = 1
door_space = 1
teacher_desk = 2

# Logic
desk_columns = int((height - min_corridor_height) / 0.7)
desk_rows = int(width / working_space_w)
total_desks = (desk_rows * desk_columns) - door_space - teacher_desk
# End of Logic

# Print Output
print(total_desks)
