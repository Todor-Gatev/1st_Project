password = input()


while True:
    command = input()
    if command == "Done":
        break

    command = command.split()
    action = command[0]

    if action == "TakeOdd":
        password = password[1::2]
        print(password)
    elif action == "Cut":
        idx, length = int(command[1]), int(command[2]),
        sub_str = password[idx:idx + length]
        password = password.replace(sub_str, '', 1)
        print(password)
    elif action == "Substitute":
        substring = command[1]
        substitute = command[2]

        if substring in password:
            password = password.replace(substring, substitute)
            print(password)
        else:
            print("Nothing to replace!")

print(f"Your password is: {password}")
