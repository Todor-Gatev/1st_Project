try:
    open('text.txt')
    print("file found")
except FileNotFoundError:
    print("file not found")

try:
    open('text1.txt')
    print("file found")
except FileNotFoundError:
    print("file not found")
