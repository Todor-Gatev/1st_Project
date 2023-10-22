from string import punctuation

with open("text.txt", "r") as input_file, open("output.txt", "w") as output_file:
    result = []
    for i, line in enumerate(input_file.readlines()):
        letters_count = 0
        punc_count = 0
        for ch in line:
            if ch.isalpha():
                letters_count += 1
            elif ch in punctuation:
                punc_count += 1
        result.append(f"Line {i + 1}: {line[:-1]} ({letters_count})({punc_count})")
    output_file.write("\n".join(result))