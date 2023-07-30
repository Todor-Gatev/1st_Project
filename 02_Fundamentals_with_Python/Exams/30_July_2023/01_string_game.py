# Read user input
text = input()

# Logic
while True:
    command = input()

    if command == "Done":
        break

    action, *info = command.split()

    if action == "Change":
        ch, replacement = info[0], info[1]
        text = text.replace(ch, replacement)
        print(text)
    elif action == "Includes":
        sub_str = info[0]

        if sub_str in text:
            print("True")
        else:
            print("False")
    elif action == "End":
        sub_str = info[0]

        if text.endswith(sub_str):
            print("True")
        else:
            print("False")
    elif action == "Uppercase":
        text = text.upper()
        print(text)
    elif action == "FindIndex":
        ch = info[0]
        print(text.find(ch))
    elif action == "Cut":
        start_idx, count = int(info[0]), int(info[1]),
        cut_chars = text[start_idx:start_idx + count]
        text = text[:start_idx] + text[start_idx + count:]
        print(cut_chars)
# End of Logic

# Print Output
