# # matrix with even elements
# matrix = [[int(x) for x in input().split(", ") if int(x) % 2 == 0] for _ in range(int(input()))]
# print(matrix)

# region flattening matrix

# # flattening matrix 2d
# matrix = [[int(j) for j in input().split(", ")] for i in range(int(input()))]
# flatten_matrix = [el for list_i in matrix for el in list_i]
# print(flatten_matrix)
# # flattening matrix 3d
# m3d = [[[k for k in range(3)] for j in range(3)] for i in range(3)]
# print(m3d)  # [[[0, 1, 2],[0, 1, 2],[0, 1, 2]],[[0, 1, 2],[0, 1, 2],[0, 1, 2]], [[0, 1, 2], [0, 1, 2], [0, 1, 2]]]
# flatten_m3d = [k for m2d in m3d for m1d in m2d for k in m1d]
# print(flatten_m3d)  # [0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2]

# endregion

# region sum of primary or secondary diagonal

n = int(input())
matrix = [[int(x) for x in input().split()] for _ in range(n)]
primary_diagonal = sum([matrix[i][i] for i in range(n)])
secondary_diagonal = sum([matrix[i][n - i - 1] for i in range(n)])
print(primary_diagonal)
print(secondary_diagonal)

# faster solution
primary_diagonal_sum = 0
secondary_diagonal_sum = 0
for i in range(n):
    row = [int(x) for x in input().split()]
    primary_diagonal_sum += row[i]
    secondary_diagonal_sum += row[n - i - 1]
print(primary_diagonal_sum)
print(secondary_diagonal_sum)

# endregion
