import re


""""It is supposed that 'text' doesn't contain numbers. Numbers are count as special symbols"""
regex_letters = re.compile(r'[A-Za-z]')
symbols = {"-", ",", ".", "!", "?"}

with open('text.txt') as text, open('output.txt', 'a') as output:
    line_num = 1

    for line in text:
        line = line[:-1]  # -1 is for \n in line
        spaces = line.count(' ')
        letters_num = len(regex_letters.findall(line))
        special_symbols = len(line) - spaces - letters_num

        output.write(f"Line {line_num}: {line} ({letters_num})({special_symbols})\n")

        line_num += 1
