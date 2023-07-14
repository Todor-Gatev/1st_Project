ch1 = input()
ch2 = input()
string = input()

test = string.split()
result = 0

for ch in string:
    if ord(ch1) < ord(ch) < ord(ch2):
        result += ord(ch)

print(result)
