import re

regex_letters = re.compile(r'[A-Za-z]')
regex_numbers = re.compile(r'[0-9]')

with open('text.txt') as text, open('output.txt', 'w') as output:
    line_number = 1

    for line in text:
        line = line[:-1]  # -1 is for \n in line
        spaces = line.count(' ')
        letters_num = len(regex_letters.findall(line))
        numbers_num = len(regex_numbers.findall(line))
        special_symbols = len(line) - spaces - letters_num - numbers_num

        output.write(f"Line {line_number}: {line} ({letters_num})({special_symbols})\n")

        line_number += 1
