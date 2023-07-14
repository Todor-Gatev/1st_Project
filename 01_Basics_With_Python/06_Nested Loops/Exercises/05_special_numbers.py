# Read user input
user_num = int(input())

# Logic
for i in range(1111, 10000):
    is_special = True
    temp_text = str(i)
    for j in temp_text:
        a = int(j)
        if a == 0:
            is_special = False
            break
        if user_num % a != 0:
            is_special = False
            break
    if is_special:
        print(i, end=' ')
# End of Logic
