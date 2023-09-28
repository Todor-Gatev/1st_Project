text = input()
symbols = {}

for ch in text:
    symbols[ch] = symbols.get(ch, 0) + 1

for ch, count in sorted(symbols.items()):
    print(f"{ch}: {count} time/s")
