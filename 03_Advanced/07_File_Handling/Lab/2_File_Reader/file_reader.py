res = 0
for line in open('numbers.txt'):
    res += int(line)

print(res)
