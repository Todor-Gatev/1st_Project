import os

command = input()

while command != "End":
    action, *info = command.split('-')

    if action == "Create":
        with open(f'{info[0]}', 'w') as file:
            pass
    elif action == "Add":
        with open(f'{info[0]}', 'a') as file:
            file.write(f"{info[1]}\n")
    elif action == "Replace":
        if os.path.isfile(f'{info[0]}'):
            with open(f'{info[0]}') as file:
                data = file.read()

            data = data.replace(info[1], info[2])

            with open(f'{info[0]}', 'w') as file:
                file.write(data)
        else:
            print("An error occurred")
    elif action == "Delete":
        if os.path.isfile(f'{info[0]}'):
            os.remove(info[0])
        else:
            print("An error occurred")
    command = input()
