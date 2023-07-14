# Read user input
first_num = int(input())
second_num = int(input())

# Logic
for i in range(first_num, second_num + 1):
    sum_one = 0
    sum_two = 0
    i_text = str(i)
    counter = 1

    for j in i_text:
        temp_num = int(j)
        if (counter % 2) == 0:
            sum_two += temp_num
            counter += 1
        else:
            sum_one += temp_num
            counter += 1

    if sum_one == sum_two:
        print(i, end=' ')
# End of Logic
