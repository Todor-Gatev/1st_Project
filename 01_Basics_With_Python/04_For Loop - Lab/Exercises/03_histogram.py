# Read user input
n = int(input())

p1 = 0
p2 = 0
p3 = 0
p4 = 0
p5 = 0

pcs_p1 = 0
pcs_p2 = 0
pcs_p3 = 0
pcs_p4 = 0
pcs_p5 = 0
# Logic
for _ in range(n):
    current_num = int(input())
    if current_num < 200:
        pcs_p1 += 1
    elif current_num < 400:
        pcs_p2 += 1
    elif current_num < 600:
        pcs_p3 += 1
    elif current_num < 800:
        pcs_p4 += 1
    else:
        pcs_p5 += 1

p1 = pcs_p1 / n * 100
p2 = pcs_p2 / n * 100
p3 = pcs_p3 / n * 100
p4 = pcs_p4 / n * 100
p5 = pcs_p5 / n * 100

# Print Output
print(f'{p1:.2f}%')
print(f'{p2:.2f}%')
print(f'{p3:.2f}%')
print(f'{p4:.2f}%')
print(f'{p5:.2f}%')
