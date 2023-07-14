# Read user input
n = int(input())

# Logic
for i in range(n):
    num = int(input())
    if num > 88:
        print("Bye.")
    elif num == 88:
        print("Hello")
    elif num == 86:
        print("How are you?")
    else:
        print("GREAT!")
# End of Logic
