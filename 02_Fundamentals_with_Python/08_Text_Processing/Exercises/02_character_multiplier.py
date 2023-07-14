str1, str2 = input().split()

result = 0
length = max(len(str1), len(str2))

if len(str1) < length:
    str1 += '' * (length - len(str1))

if len(str2) < length:
    str2 += '' * (length - len(str2))

for i in range(length):
    result += ord(str1[i]) * ord(str2[i])

print(result)
