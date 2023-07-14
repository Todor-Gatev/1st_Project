text = input().replace(' ', '')

count_chars = {}

for ch in text:
    if ch not in count_chars:
        count_chars[ch] = 0
    count_chars[ch] += 1

for key, value in count_chars.items():
    print(f"{key} -> {value}")
