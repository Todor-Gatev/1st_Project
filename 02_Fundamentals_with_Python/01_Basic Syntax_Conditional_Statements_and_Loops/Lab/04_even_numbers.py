# Read user input
n = int(input())

# Logic
for i in range(n):
    temp_n = int(input())

    if temp_n % 2 != 0:
        print(f"{temp_n} is odd!")
        break
else:
    print("All numbers are even.")
# End of Logic
