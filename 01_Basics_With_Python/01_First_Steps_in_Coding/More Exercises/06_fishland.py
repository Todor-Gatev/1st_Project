# Read user input
mackerel_price = float(input())
sprat_price = float(input())
bonito_kg = float(input())
scad_kg = float(input())
mussel_kg = int(input())

# Parameters
bonito_price = 1.6 * mackerel_price
scad_price = 1.8 * sprat_price
mussel_price = 7.5

# Logic
total_price = bonito_kg * bonito_price + \
              scad_kg * scad_price + \
              mussel_price * mussel_kg
# End of Logic

# Print Output
print(f'{total_price:.2f}')
