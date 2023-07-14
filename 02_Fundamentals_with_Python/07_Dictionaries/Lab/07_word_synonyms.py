n = int(input())

dictionary = {}

for _ in range(n):
    key = input()
    value = input()

    if key not in dictionary:
        dictionary[key] = [value]
    else:
        dictionary[key].append(value)

for key, value in dictionary.items():
    print(f"{key} - {', '.join(value)}")
