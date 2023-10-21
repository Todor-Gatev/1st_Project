players = {p: False for p in input().split(", ")}

maze = [input().split() for _ in range(6)]

while True:
    for p in players:
        info = input()
        i, j = int(info[1]), int(info[4]),

        if players[p]:
            players[p] = not players[p]
            continue
        elif maze[i][j] == 'W':
            print(f"{p} hits a wall and needs to rest.")
            players[p] = True
        elif maze[i][j] == 'T':
            winner = "Tom" if p == "Jerry" else "Jerry"
            print(f"{p} is out of the game! The winner is {winner}.")
            exit()
        elif maze[i][j] == 'E':
            print(f"{p} found the Exit and wins the game!")
            exit()
