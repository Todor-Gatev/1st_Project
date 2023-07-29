import re

text = input()

places = []
travel_points = 0

result = re.finditer(r"([=/])(?P<place>[A-Z][A-Za-z]{2,})\1", text)

for res in result:
    place = res.group("place")
    places.append(place)
    travel_points += len(place)

print(f"Destinations: {', '.join(places)}")
print(f"Travel Points: {travel_points}")
