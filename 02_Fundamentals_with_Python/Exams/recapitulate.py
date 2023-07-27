heroes = {}

for _ in range(int(input())):
    name, hit_points, mana_points = input().split()
    hit_points, mana_points = int(hit_points), int(mana_points),

    heroes[name] = [hit_points, mana_points]

while True:
    command = input()

    if command == "End":
        break

    command = command.split(" - ")
    action, name = command[0], command[1],

    if action == "CastSpell":
        mp_needed, spell_name = int(command[2]), command[3],

        if mp_needed <= heroes[name][1]:
            heroes[name][1] -= mp_needed
            print(f"{name} has successfully cast {spell_name} and now has {heroes[name][1]} MP!")
        else:
            print(f"{name} does not have enough MP to cast {spell_name}!")
    elif action == "TakeDamage":
        damage, attacker = int(command[2]), command[3]

        if heroes[name][0] > damage:
            heroes[name][0] -= damage
            print(f"{name} was hit for {damage} HP by {attacker} and now has {heroes[name][0]} HP left!")
        else:
            heroes.pop(name)
            print(f"{name} has been killed by {attacker}!")
    elif action == "Recharge":
        amount = int(command[2])

        if amount + heroes[name][1] > 200:
            amount = 200 - heroes[name][1]

        heroes[name][1] += amount
        print(f"{name} recharged for {amount} MP!")
    elif action == "Heal":
        amount = int(command[2])

        if amount + heroes[name][0] > 100:
            amount = 100 - heroes[name][0]

        heroes[name][0] += amount
        print(f"{name} healed for {amount} HP!")

for name, values in heroes.items():
    print(f"{name}\n  HP: {values[0]}\n  MP: {values[1]}")
