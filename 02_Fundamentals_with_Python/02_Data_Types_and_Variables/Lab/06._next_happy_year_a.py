# Read user input
year = int(input())

# Logic
while True:
    year += 1
    digit = year

    while digit:
        d_last = str(digit % 10)
        digit = digit // 10

        if d_last not in str(digit):
            continue
        else:
            break
    else:
        print(year)
        exit()
# End of Logic
