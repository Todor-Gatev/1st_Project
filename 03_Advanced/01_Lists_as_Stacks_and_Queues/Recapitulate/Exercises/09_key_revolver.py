from collections import deque

bullet_price = int(input())
gun_barrel_size = int(input())
bullets = [int(x) for x in input().split()]
locks = deque(int(x) for x in input().split())
money_earned = int(input())

while bullets:
    bullets_in_barrel = min(len(bullets), gun_barrel_size)

    for idx in range(bullets_in_barrel):
        bullet = bullets.pop()
        money_earned -= bullet_price

        if bullet > locks[0]:
            print("Ping!")
        else:
            locks.popleft()
            print("Bang!")

        if idx == gun_barrel_size - 1 and bullets:
            print("Reloading!")

        if not locks:
            print(f"{len(bullets)} bullets left. Earned ${money_earned}")
            exit()

print(f"Couldn't get through. Locks left: {len(locks)}")
