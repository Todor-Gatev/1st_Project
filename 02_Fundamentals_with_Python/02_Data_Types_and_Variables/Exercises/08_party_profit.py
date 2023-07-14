# Read user input
# group_size = int(input())
companions_count = int(input())
days = int(input())

# Parameters

# Variables
coins = 0
# companions_count = group_size #- 1

# Logic
for i in range(1, days + 1):
    if i % 10 == 0:
        companions_count -= 2

    if i % 15 == 0:
        companions_count += 5
    coins += 50 - 2 * companions_count

    if i % 3 == 0:
        coins -= 3 * companions_count

    if i % 5 == 0:
        coins += 20 * companions_count
        if i % 3 == 0:
            coins -= 2 * companions_count
# End of Logic

# Print Output
print(f"{companions_count} companions received "
      f"{int(coins / companions_count)} coins each.")
