heroes = {}

for _ in range(int(input())):
    info = input().split()
    hp_points = min(100, int(info[1]))
    mp_points = min(200, int(info[2]))
    heroes[info[0]] = [hp_points, mp_points]

while True:
    command = input()

    if command == "End":
        break

    command = command.split(" - ")
    action = command[0]
    name = command[1]

    if action == "CastSpell":
        mp_needed = int(command[2])
        spell_name = command[3]
        if mp_needed <= heroes[name][1]:
            heroes[name][1] -= mp_needed
            print(f"{name} has successfully cast {spell_name} and now has {heroes[name][1]} MP!")
        else:
            print(f"{name} does not have enough MP to cast {spell_name}!")
    elif action == "TakeDamage":
        damage_hp = int(command[2])
        attacker = command[3]
        if int(heroes[name][0]) > damage_hp:
            heroes[name][0] -= damage_hp
            print(f"{name} was hit for {damage_hp} HP by {attacker} and now has {heroes[name][0]} HP left!")
        else:
            print(f"{name} has been killed by {attacker}!")
            heroes.pop(name)
    elif action == "Recharge":
        amount = int(command[2])
        if heroes[name][1] + amount > 200:
            amount = 200 - heroes[name][1]

        heroes[name][1] += amount
        print(f"{name} recharged for {amount} MP!")
    elif action == "Heal":
        amount = int(command[2])
        if heroes[name][0] + amount > 100:
            amount = 100 - heroes[name][0]

        heroes[name][0] += amount
        print(f"{name} healed for {amount} HP!")

for name, value in heroes.items():
    print(name)
    print(f"  HP: {value[0]}")
    print(f"  MP: {value[1]}")
