symbols = {"-", ",", ".", "!", "?"}

with open('text.txt') as t:
    i = 0

    for line in t:
        if i % 2 == 0:
            for ch in symbols:
                line = line.replace(ch, '@')

            line = line.split()
            line.reverse()
            print(*line)

        i += 1
