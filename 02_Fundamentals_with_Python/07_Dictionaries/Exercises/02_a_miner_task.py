text = input()

resources = {}

while text != "stop":
    key = text
    value = int(input())

    if key not in resources:
        resources[key] = 0

    resources[key] += value
    text = input()

for key, value in resources.items():
    print(f"{key} -> {value}")
