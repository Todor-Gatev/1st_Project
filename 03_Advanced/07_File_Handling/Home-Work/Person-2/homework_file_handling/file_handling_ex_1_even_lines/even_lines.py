with open('text.txt') as f:
    for index, line in enumerate(f.readlines()):
        if index % 2 == 0:
            for character in ["-", ",", ".", "!", "?"]:
                line = line.replace(character, '@')
            print(' '.join(reversed(line.split())))
