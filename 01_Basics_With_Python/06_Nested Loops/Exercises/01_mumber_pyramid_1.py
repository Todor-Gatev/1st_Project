# Read user input
input_number = int(input())

# Logic
counter = 1
all_is_printed = False
row_num = 1

for i in range(input_number):
    for j in range(1, row_num + 1):
        if counter > input_number:
            all_is_printed = True
            break
        else:
            print(counter, end=' ')
            counter += 1

    if all_is_printed:
        break
    print()
    row_num += 1
