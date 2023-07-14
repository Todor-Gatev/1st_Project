# Read user input
int_list = [int(x) for x in input().split(", ")]
int_list.reverse()
groups = (max(int_list) + 9) // 10

# Logic
for i in range(1, groups + 1):
    list_of_numbers = []
    for index in range(len(int_list) - 1, -1, -1):
        if int_list[index] <= i * 10:
            list_of_numbers.append(int_list[index])
            int_list.remove(int_list[index])

    print(f"Group of {i * 10}'s: {list_of_numbers}")
# End of Logic
