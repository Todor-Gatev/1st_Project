with open('text.txt') as t:
    i = 0

    for line in t:
        if i % 2 == 0:
            line = line.replace('-', '@')
            line = line.replace(',', '@')
            line = line.replace('.', '@')
            line = line.replace('!', '@')
            line = line.replace('?', '@')
            line = line.split()
            line.reverse()
            print(*line)

        i += 1
