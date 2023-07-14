# Read user input
population = [int(x) for x in input().split(", ")]
min_wealth = int(input())

# Logic
average = sum(population) / len(population)

if average < min_wealth:
    print("No equal distribution possible")
    exit()

for i in range(len(population)):
    if population[i] < min_wealth:
        taxes = min_wealth - population[i]
        population[i] = min_wealth

        while taxes:
            max_wealth = max(population)
            idx = population.index(max_wealth)

            if population[idx] - taxes > min_wealth:
                population[idx] -= taxes
                taxes = 0
            else:
                taxes -= population[idx] - min_wealth
                population[idx] = min_wealth

# End of Logic

# Print Output
print(population)
