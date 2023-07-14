# Read user input
age = int(input())
washing_machine_price = float(input())
toy_price = int(input())

# Logic
toys_pcs = 0
savings = 0

for i in range(1, age + 1):
    if i % 2 == 0:
        savings += 9 + (i - 2) / 2 * 10
    else:
        toys_pcs += 1

total_savings = savings + toys_pcs * toy_price
diff = abs(total_savings - washing_machine_price)

if total_savings < washing_machine_price:
    print(f'No! {diff:.2f}')
else:
    print(f'Yes! {diff:.2f}')
