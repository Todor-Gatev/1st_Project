# # matrix with even elements
# matrix = [[int(x) for x in input().split(", ") if int(x) % 2 == 0] for _ in range(int(input()))]
# print(matrix)
#
# # flattening matrix 2d
# matrix = [[int(j) for j in input().split(", ")] for i in range(int(input()))]
# flatten_matrix = [el for list_i in matrix for el in list_i]
# print(flatten_matrix)
# flattening matrix 3d
m3d = [[[k for k in range(3)] for j in range(3)] for i in range(3)]
print(m3d)  # [[[0, 1, 2], [0, 1, 2], [0, 1, 2]], [[0, 1, 2], [0, 1, 2], [0, 1, 2]], [[0, 1, 2], [0, 1, 2], [0, 1, 2]]]
flatten_m3d = [k for m2d in m3d for list_i in m2d for k in list_i]
print(flatten_m3d)  # [0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2]
