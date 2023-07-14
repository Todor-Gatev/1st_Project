# Read user input
user_num = int(input())

# Logic
for i in range(1111, 10000):
    for j in str(i):
        if j == '0':
            break
        if user_num % int(j) != 0:
            break
    else:
        print(i, end=' ')
# End of Logic
