data = input().lower().split()

words_dict = dict.fromkeys(data, 0)

for el in data:
    words_dict[el] += 1

for key, value in words_dict.data():
    if value % 2 != 0:
        print(key, end=' ')
