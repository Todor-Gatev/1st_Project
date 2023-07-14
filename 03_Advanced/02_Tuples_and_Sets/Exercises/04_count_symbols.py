from collections import defaultdict

text = input()
symbols = defaultdict(int)

for ch in text:
    symbols[ch] += 1

symbols = dict(sorted(symbols.items()))

for ch, count in symbols.items():
    print(f"{ch}: {count} time/s")
