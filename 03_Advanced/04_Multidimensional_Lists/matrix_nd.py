# https://www.educba.com/3d-arrays-in-python/
# https://www.educba.com/multidimensional-array-in-python/
n = int(input())
matrix_2d = [[int(x) for x in input().split(", ")] for _ in range(n)]
# matrix_2d = [list(map(int, input().split(", "))) for list_n in range(n)]
# matrix_2d = [[1, 2, 3], [4, 5, 6]]
flatten_matrix = [el for list_i in matrix_2d for el in list_i]
# flatten_matrix = []
# for list_i in matrix_2d:
#     flatten_matrix.extend(list_i)
#     # flatten_matrix += list_i
# for i in range(len(matrix_2d)):
#     flatten_matrix.extend(matrix_2d[i])
#     # flatten_matrix += matrix_2d[i]
print(flatten_matrix)
