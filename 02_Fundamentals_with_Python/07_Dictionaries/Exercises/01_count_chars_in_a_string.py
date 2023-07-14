text = input().replace(' ', '')
text_list = []
text_list += text

count_chars = dict.fromkeys(text_list, 0)

for ch in text_list:
    count_chars[ch] += 1

for key, value in count_chars.data():
    print(f"{key} -> {value}")
