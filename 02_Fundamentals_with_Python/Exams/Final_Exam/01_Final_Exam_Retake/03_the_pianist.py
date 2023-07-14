n = abs(int(input()))

pieces = {}

for _ in range(n):
    piece, composer, key = input().split("|")
    pieces.update({piece: [composer, key]})
    # pieces.setdefault(piece, [composer, key])
    # pieces[piece] = [composer, key]

command = input()

while command != "Stop":
    command = command.split("|")
    action = command[0]

    if action == "Add":
        piece, composer, key = command[1], command[2], command[3]
        if piece not in pieces:
            pieces[piece] = [composer, key]
            print(f"{piece} by {composer} in {key} added to the collection!")
        else:
            print(f"{piece} is already in the collection!")
    elif action == "Remove":
        piece = command[1]
        if piece not in pieces:
            print(f"Invalid operation! {piece} does not exist in the collection.")
        else:
            pieces.pop(piece)
            print(f"Successfully removed {piece}!")
    elif action == "ChangeKey":
        piece, new_key = command[1], command[2]
        if piece in pieces:
            pieces[piece][1] = new_key
            print(f"Changed the key of {piece} to {new_key}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")

    command = input()

for piece, value in pieces.items():
    print(f"{piece} -> Composer: {value[0]}, Key: {value[1]}")
