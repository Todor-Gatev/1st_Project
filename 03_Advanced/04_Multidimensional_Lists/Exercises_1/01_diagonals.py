n = int(input())

matrix = [[int(x) for x in input().split(", ")] for _ in range(n)]

primary_diagonal = []
secondary_diagonal = []

for i in range(n):
    primary_diagonal.append(matrix[i][i])
    secondary_diagonal.append(matrix[i][n - i - 1])

print(f"Primary diagonal: {', '.join(str(x) for x in primary_diagonal)}. Sum: {sum(primary_diagonal)}")
print(f"Secondary diagonal: {', '.join(str(x) for x in secondary_diagonal)}. Sum: {sum(secondary_diagonal)}")


# solution 2 - without matrix; one loop less;
# n = int(input())
#
# primary_diagonal = []
# secondary_diagonal = []
#
# # for i in range(n):
# #     row = [int(x) for x in input().split(",")]
# #     primary_diagonal.append(row[i])
# #     secondary_diagonal.append(row[n - i - 1])
#
# print(f"Primary diagonal: {', '.join(str(x) for x in primary_diagonal)}. Sum: {sum(primary_diagonal)}")
# print(f"Secondary diagonal: {', '.join(str(x) for x in secondary_diagonal)}. Sum: {sum(secondary_diagonal)}")
