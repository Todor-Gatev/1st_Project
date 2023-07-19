# solution - without matrix; one loop less;
n = int(input())

primary_diagonal_sum = 0
secondary_diagonal_sum = 0

for i in range(n):
    row = [int(x) for x in input().split()]

    primary_diagonal_sum += row[i]
    secondary_diagonal_sum += row[n - i - 1]

print(abs(primary_diagonal_sum - secondary_diagonal_sum))


# solution 2 - with matrix; one loop more;
# n = int(input())
#
# matrix = [[int(x) for x in input().split()] for _ in range(n)]
#
# primary_diagonal_sum = 0
# secondary_diagonal_sum = 0
#
# for i in range(n):
#     primary_diagonal_sum += matrix[i][i]
#     secondary_diagonal_sum += matrix[i][n - i - 1]
#
# print(abs(primary_diagonal_sum - secondary_diagonal_sum))
