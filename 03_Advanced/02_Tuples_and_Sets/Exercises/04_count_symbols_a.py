text = input()
symbols = {}

for ch in text:
    symbols[ch] = symbols.get(ch, 0) + 1

# symbols = dict(sorted(symbols.items()))
#
# for ch, count in symbols.items():
#     print(f"{ch}: {count} time/s")

for ch, count in sorted(symbols.items()):
    print(f"{ch}: {count} time/s")
