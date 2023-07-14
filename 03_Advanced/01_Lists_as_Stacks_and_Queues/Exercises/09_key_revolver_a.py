from collections import deque

price_of_bullet = int(input())
gun_barrel_size = int(input())
bullets = list(map(int, input().split()))
locks = deque(map(int, input().split()))
value = int(input())

while bullets:
    bullets_reloading = min(gun_barrel_size, len(bullets))
    for idx in range(bullets_reloading):
        bullet = bullets.pop()
        value -= price_of_bullet
        if bullet <= locks[0]:
            locks.popleft()
            print("Bang!")
            if not locks:
                if bullets and idx == bullets_reloading - 1:
                    print("Reloading!")

                print(f"{len(bullets)} bullets left. Earned ${value}")
                exit()
        else:
            print("Ping!")

    if bullets:
        print("Reloading!")

print(f"Couldn't get through. Locks left: {len(locks)}")
