# Read user input
int_list = [int(x) for x in input().split()]


# Variables
int_list.sort(reverse=True)
average = sum(int_list) / len(int_list)
top_5 = []
over_average_counter = 0

# Logic
for num in int_list:
    if num > average:
        top_5.append(num)
        over_average_counter += 1

        if over_average_counter == 5:
            break
# End of Logic

# Print Output
if top_5:
    top_5_str = [str(x) for x in top_5]
    print(' '.join(top_5_str))
else:
    print("No")
