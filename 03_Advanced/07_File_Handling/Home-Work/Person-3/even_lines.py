with open("text.txt", "r") as f:
    for i, line in enumerate(f.readlines()):
        if i % 2 == 0:
            for ch in "-,.!?":
                line = line.replace(ch, "@")
            print(" ".join(reversed(line.split())))