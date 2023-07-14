country_names = input().split(', ')
capital_names = input().split(', ')
# capital_cities = {country: capital for (country, capital)
#                   in zip(country_names, capital_names)}
# capital_cities = dict(zip(input().split(', '), input().split(', ')))
# capital_cities = {country_names[idx]: capital_names[idx] for idx in range(len(country_names))}
capital_cities = dict(zip(country_names, capital_names))

for country, capital_city in capital_cities.items():
    print(f"{country} -> {capital_city}")
