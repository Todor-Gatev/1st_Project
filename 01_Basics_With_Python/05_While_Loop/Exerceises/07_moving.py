# Read user input
wide = int(input())
length = int(input())
height = int(input())

# Logic
volume = wide * length * height
input_data = ''
free_volume = volume
carton_count = 0

while True:
    input_data = input()
    if input_data == "Done":
        # TODO: Check the other cases…
        print(f"{free_volume} Cubic meters left.")
        break
    else:
        input_data = int(input_data)
        free_volume -= input_data
    if free_volume < 0:
        print(f"No more free space! You need {-free_volume} Cubic meters more.")
        break

# Print Output
