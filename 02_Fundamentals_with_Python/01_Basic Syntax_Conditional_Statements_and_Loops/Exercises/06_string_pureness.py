# Read user input
n = int(input())

# Logic
for i in range(n):
    text = input()
    for char in text:
        if char == ',' or char == '.' or char == '_':
            print(f"{text} is not pure!")
            break
    else:
        print(f"{text} is pure.")
# End of Logic
