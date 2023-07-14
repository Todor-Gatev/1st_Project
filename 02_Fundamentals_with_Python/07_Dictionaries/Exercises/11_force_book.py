data = input()

force_book = {}

while data != "Lumpawaroo":
    if '|' in data:
        force_side, force_user = data.split(' | ')

        if force_side not in force_book:
            force_book[force_side] = []

        for force_side in force_book:
            if force_user not in force_book[force_side]:
                continue
            else:
                break
        else:
            force_book[force_side].append(force_user)
    elif "->" in data:
        force_user, force_side = data.split(" -> ")

        for side in force_book:
            if force_user in force_book[side]:
                force_book[side].remove(force_user)
                break

        if force_side not in force_book:
            force_book[force_side] = []

        force_book[force_side].append(force_user)
        print(f"{force_user} joins the {force_side} side!")

    data = input()

for force_side in force_book:
    force_users_count = len(force_book[force_side])
    if force_users_count > 0:
        print(f"Side: {force_side}, Members: {force_users_count}")

    for force_user in force_book[force_side]:
        print(f"! {force_user}")
