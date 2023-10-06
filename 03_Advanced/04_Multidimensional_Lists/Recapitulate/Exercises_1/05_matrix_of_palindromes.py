rows, cols = [int(x) for x in input().split()]

for i in range(97, 97 + rows):
    print(*[chr(i) + chr(i + j) + chr(i) for j in range(cols)])
