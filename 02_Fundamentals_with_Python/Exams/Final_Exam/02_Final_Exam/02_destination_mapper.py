import re

places = input()

destinations = []
travel_points = 0

# (?P<sep>[=/])(?P<location>[A-Z][A-Za-z]{2,})(?P=sep)
pattern = r"(?P<sep>[=/])(?P<location>[A-Z][A-Za-z]{2,})(?P=sep)"
result = re.finditer(pattern, places)
for res in result:
    destination = res.group("location")
    destinations.append(destination)
    travel_points += len(destination)

print("Destinations: ", end='')
print(*destinations, sep=", ")
print(f"Travel Points: {travel_points}")
