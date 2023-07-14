message = input()

command = input()

while command != "Decode":
    command = command.split('|')
    action = command[0]
    if action == "Move":
        num_of_letters = int(command[1])
        n_letters = message[:num_of_letters]
        message = message[num_of_letters:] + n_letters
    elif action == "Insert":
        index = int(command[1])
        value = command[2]
        message = message[:index] + value + message[index:]
    elif action == "ChangeAll":
        substring = command[1]
        replacement = command[2]
        message = message.replace(substring, replacement)
    command = input()

print(f"The decrypted message is: {message}")
