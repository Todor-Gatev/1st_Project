# Read user input
# , hay, and cover
food = float(input())
hay = float(input())
cover = float(input())
weight = float(input())

# Variables

# Logic
for day in range(1, 31):
    food -= 0.3
    if food < 0:
        print("Merry must go to the pet store!")
        break
    if day % 2 == 0:
        hay -= 0.05 * food
        if hay < 0:
            print("Merry must go to the pet store!")
            break
    if day % 3 == 0:
        cover -= weight / 3
        if cover < 0:
            print("Merry must go to the pet store!")
            break
else:
    print(f"Everything is fine! Puppy is happy! Food: "
          f"{food:.2f}, Hay: {hay:.2f}, Cover: {cover:.2f}.")
# End of Logic

# Print Output
