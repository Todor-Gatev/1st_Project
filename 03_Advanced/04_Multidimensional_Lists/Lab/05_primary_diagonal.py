n = int(input())

matrix = [[int(x) for x in input().split()] for _ in range(n)]

primary_diagonal = sum([matrix[i][i] for i in range(n)])

print(primary_diagonal)

# secondary_diagonal = 0
#
# for i in range(n):
#     j = n - 1 - i
#     secondary_diagonal += matrix[i][j]
#
# print(secondary_diagonal)
