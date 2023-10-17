from collections import deque

textiles = deque(int(x) for x in input().split())
medicament = [int(x) for x in input().split()]
items = {}

while textiles and medicament:
    t = textiles.popleft()
    m = medicament.pop()

    sum_res = m + t

    if sum_res == 30:
        items["Patch"] = items.get("Patch", 0) + 1
    elif sum_res == 40:
        items["Bandage"] = items.get("Bandage", 0) + 1
    elif sum_res >= 100:
        items["MedKit"] = items.get("MedKit", 0) + 1

        if sum_res - 100:
            medicament[-1] += sum_res - 100
    else:
        medicament.append(m + 10)

if not textiles and not medicament:
    print("Textiles and medicaments are both empty.")
elif not textiles:
    print("Textiles are empty.")
else:
    print("Medicaments are empty.")

sorted_items = sorted(items.items(), key=lambda x: (-x[1], x[0],))
[print(f"{item} - {amount}") for item, amount in sorted_items]

if medicament:
    medicament.reverse()
    print(f"Medicaments left: {', '.join(str(x) for x in medicament)}")

if textiles:
    print(f"Textiles left: {', '.join(str(x) for x in textiles)}")
