from collections import deque

bullet_price = int(input())
gun_barrel_size = int(input())
bullets = [int(x) for x in input().split()]
locks = deque(int(x) for x in input().split())
value_of_the_intelligence = int(input())

left_bullets_in_barrel = gun_barrel_size
received_bullets = len(bullets)

while bullets and locks:
    left_bullets_in_barrel -= 1
    bullet = bullets.pop()
    if bullet <= locks[0]:
        locks.popleft()
        print("Bang!")
    else:
        print("Ping!")

    if left_bullets_in_barrel == 0 and bullets:
        left_bullets_in_barrel = min(gun_barrel_size, len(bullets))
        print("Reloading!")

if not locks:
    bullets_left = len(bullets)
    total_bullet_price = bullet_price * (received_bullets - bullets_left)
    money_earned = value_of_the_intelligence - total_bullet_price
    print(f"{bullets_left} bullets left. Earned ${money_earned}")
else:
    print(f"Couldn't get through. Locks left: {len(locks)}")
