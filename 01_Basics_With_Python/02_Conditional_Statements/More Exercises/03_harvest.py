from math import ceil

# Read user input
vineyard_sqm = int(input())   # sqm
grape_kg_per_sqm = float(input())
needed_vine = int(input())  # liters
workers = int(input())    # number

# Parameters
grape_kg_for_vine = 0.4 * (grape_kg_per_sqm * vineyard_sqm)
produced_vine = grape_kg_for_vine / 2.5

diff = produced_vine - needed_vine

# Logic
if diff < 0:
    print(f'It will be a tough winter! More {int(abs(diff))} liters wine needed.')
else:
    liters_per_worker = diff / workers
    print(f'Good harvest this year! Total wine: {int(produced_vine)} liters.')
    print(f'{ceil(diff)} liters left -> {ceil(liters_per_worker)} liters per person.')

# End of Logic

# Print Output
