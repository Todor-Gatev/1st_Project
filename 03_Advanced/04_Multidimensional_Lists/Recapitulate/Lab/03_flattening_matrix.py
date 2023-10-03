matrix = [[int(j) for j in input().split(", ")] for i in range(int(input()))]
flatten_matrix = [el for list_i in matrix for el in list_i]

print(flatten_matrix)
