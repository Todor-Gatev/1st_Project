def forecast(*args):
    result = []
    weather = {
        "Sunny": [],
        "Cloudy": [],
        "Rainy": [],
    }

    for info in args:
        weather[info[1]].append(info[0])

    for key, locations in weather.items():
        locations.sort()
        result.extend(f"{location} - {key}" for location in locations)

    return "\n".join(result)


# print(forecast(
#     ("Sofia", "Sunny"),
#     ("London", "Cloudy"),
#     ("New York", "Sunny")))

# print(forecast(
#     ("Beijing", "Sunny"),
#     ("Hong Kong", "Rainy"),
#     ("Tokyo", "Sunny"),
#     ("Sofia", "Cloudy"),
#     ("Peru", "Sunny"),
#     ("Florence", "Cloudy"),
#     ("Bourgas", "Sunny")))

# print(forecast(
#     ("Tokyo", "Rainy"),
#     ("Sofia", "Rainy")))
