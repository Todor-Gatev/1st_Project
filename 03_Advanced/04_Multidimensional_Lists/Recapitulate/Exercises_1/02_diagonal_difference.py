n = int(input())

diff = 0

for i in range(n):
    line = [int(x) for x in input().split()]
    diff += line[i] - line[n - 1 - i]

print(abs(diff))
