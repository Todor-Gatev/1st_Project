
num = int(input())

three_num_lis = [0, 0, 1]
print(1, end=' ')

for i in range(1, num):
    print(sum(three_num_lis), end=' ')
    three_num_lis.append(sum(three_num_lis))
    three_num_lis.pop(0)
