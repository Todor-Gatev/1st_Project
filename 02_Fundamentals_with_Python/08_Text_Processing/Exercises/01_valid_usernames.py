names = input().split(", ")

for name in names:
    if 3 <= len(name) <= 16:
        temp_name = name.replace('-', '')
        temp_name = temp_name.replace('_', '')
        if temp_name.isalnum():
            print(name)
