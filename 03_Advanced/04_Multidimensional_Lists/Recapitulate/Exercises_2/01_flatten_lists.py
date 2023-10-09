matrix = [i.split() for i in input().split('|')][::-1]

[print(x, end=' ') for row in matrix for x in row]
