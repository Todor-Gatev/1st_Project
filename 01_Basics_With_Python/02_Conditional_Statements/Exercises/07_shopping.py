# Read user input
budget = float(input())
graphic_card_pcs = int(input())
processor_pcs = int(input())
memory_pcs = int(input())

# Logic
cost_graphic_card = graphic_card_pcs * 250
cost_processor = processor_pcs * cost_graphic_card * 0.35
cost_memory = memory_pcs * cost_graphic_card * 0.1
price = cost_graphic_card + cost_processor + cost_memory

if graphic_card_pcs > processor_pcs:
    price = price * (1 - 0.15)

# Print Output
if price > budget:
    print(f"Not enough money! You need {price - budget:.2f} leva more!")
else:
    print(f"You have {budget - price:.2f} leva left!")
