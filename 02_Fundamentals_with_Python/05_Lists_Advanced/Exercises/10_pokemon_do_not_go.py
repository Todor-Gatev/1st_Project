def increase_or_decrease(a_list, number, summed):
    summed += number

    for i in range(len(a_list)):
        if a_list[i] > number:
            a_list[i] -= number
        else:
            a_list[i] += number

    return a_list, summed


# Read user input
int_list = [int(x) for x in input().split()]


# Variables
summed_value = 0

# Logic
while int_list:
    index = int(input())
    if index < 0:
        num = int_list[0]
        int_list.pop(0)
        int_list.insert(0, int_list[-1])
        int_list, summed_value = increase_or_decrease(int_list, num, summed_value)
    elif index > len(int_list) - 1:
        num = int_list[-1]
        int_list.pop(-1)
        int_list.append(int_list[0])
        int_list, summed_value = increase_or_decrease(int_list, num, summed_value)
    else:
        num = int_list[index]
        int_list.pop(index)
        int_list, summed_value = increase_or_decrease(int_list, num, summed_value)
# End of Logic

# Print Output
print(summed_value)
