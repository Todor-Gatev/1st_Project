import re

text = input()

mirror_words = []
count_word_pairs = 0

# (?P<sep>[#@])(?P<word1>[A-Za-z]{3,})(?P=sep)(?P=sep)(?P<word2>[A-Za-z]{3,})(?P=sep)
regex = re.compile(r"(?P<sep>[#@])(?P<word1>[A-Za-z]{3,})(?P=sep)(?P=sep)"
                   r"(?P<word2>[A-Za-z]{3,})(?P=sep)")

if not regex.search(text):
    print("No word pairs found!")
    print("No mirror words!")
    exit()

word_pairs = regex.finditer(text)

for word_pair in word_pairs:
    count_word_pairs += 1
    word1 = word_pair.group("word1")
    word2 = word_pair.group("word2")
    if word1 == word2[::-1]:
        mirror_words.append(f"{word1} <=> {word2}")

print(f"{count_word_pairs} word pairs found!")

if mirror_words:
    print("The mirror words are:")
    print(*mirror_words, sep=', ')
else:
    print("No mirror words!")
