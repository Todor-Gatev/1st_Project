# Read user input
wide = int(input())
length = int(input())

# Logic
available_pcs = wide * length
pcs_count = 0

while available_pcs >= pcs_count:
    input_data = input()

    if input_data == 'STOP':
        diff = available_pcs - pcs_count
        print(f"{diff} pieces are left.")
        break
    else:
        pcs_count += int(input_data)

else:
    diff = pcs_count - available_pcs
    print(f"No more cake left! You need {diff} pieces more.")

# Print Output
