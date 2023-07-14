# Read user input
chrysanthemums = int(input())
roses = int(input())
tulips = int(input())
season = input()
holiday = input()

# Parameters
bouquet_price = 2

# Variables
chrysanthemum_price = 0
rose_price = 0
tulip_price = 0

price = 0

# Logic
if season == 'Spring' or season == 'Summer':
    chrysanthemum_price = 2.00
    rose_price = 4.10
    tulip_price = 2.50
elif season == 'Autumn' or season == 'Winter':
    chrysanthemum_price = 3.75
    rose_price = 4.50
    tulip_price = 4.15

price = chrysanthemum_price * chrysanthemums \
        + rose_price * roses \
        + tulip_price * tulips

if holiday == 'Y':
    price *= 1.15

if tulips > 7 and season == 'Spring':
    price *= 0.95

if roses >= 10 and season == 'Winter':
    price *= 0.90

if (chrysanthemums + roses + tulips) > 20:
    price *= 0.80

price += 2

# End of Logic

# •	На четвъртия ред е посочен сезона – [Spring, Summer, Аutumn, Winter]
# •	На петия ред е посочено дали денят е празник – [Y – да / N - не]

# Print Output
print(f'{price:.2f}')
