import re

words = open('words.txt')
input_text = open('input.txt')

searched_words = []
result_as_dict = {}


regex = r"[A-Za-z']+"
input_words = re.findall(regex, input_text.read())

for idx in range(len(input_words)):
    input_words[idx] = input_words[idx].lower()

for line in words:
    searched_words.extend(line.split())

# input_text_list = []
# for line in input_text:
#     input_text_list.extend(line.split())

for word in searched_words:
    result_as_dict[word.lower()] = input_words.count(word.lower())

result_as_dict = dict(sorted(result_as_dict.items(), key=lambda x: (-x[1], x[0])))

for word, count in result_as_dict.items():
    with open('output.txt', 'a') as output:
        output.write(f"{word} - {count}\n")

words.close()
input_text.close()
