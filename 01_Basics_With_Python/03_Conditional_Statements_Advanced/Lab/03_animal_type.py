# Read user input
animal = input()

# Logic
if animal == "dog":
    print("mammal")
elif animal == "crocodile" \
        or animal == "snake" \
        or animal == "tortoise":
    print("reptile")
else:
    print("unknown")
