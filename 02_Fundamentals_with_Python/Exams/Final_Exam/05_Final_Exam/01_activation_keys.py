raw_key = input()

while True:
    command = input()
    if command == "Generate":
        break

    command = command.split(">>>")
    action = command[0]
    if action == "Contains":
        substring = command[1]
        if substring in raw_key:
            print(f"{raw_key} contains {substring}")
        else:
            print("Substring not found!")
    elif action == "Flip":
        start_index, end_index = int(command[2]), int(command[3])
        if command[1] == "Upper":
            raw_key = raw_key[:start_index] + \
                      raw_key[start_index:end_index].upper() + \
                      raw_key[end_index:]
        elif command[1] == "Lower":
            raw_key = raw_key[:start_index] + \
                      raw_key[start_index:end_index].lower() + \
                      raw_key[end_index:]
        print(raw_key)
    elif action == "Slice":
        start_index, end_index = int(command[1]), int(command[2]),
        raw_key = raw_key[:start_index] + raw_key[end_index:]
        print(raw_key)

print(f"Your activation key is: {raw_key}")
