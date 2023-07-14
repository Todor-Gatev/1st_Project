def get_best_sequence(half, char):
    count = 0
    result = 0
    for i in range(10):
        if half[i] == char:
            count += 1
        else:
            count = 0

        result = max(result, count)
    return result


tickets = input().split(", ")

symbols = ['@', '#', '$', '^']
is_winning = False
is_jackpot = False

for ticket in tickets:
    ticket = ticket.strip()
    if len(ticket) != 20:
        print("invalid ticket")
        continue

    half1 = ticket[:10]
    half2 = ticket[10:]
    sequence = 0
    symbol = ''

    for symbol in symbols:
        sequence1 = get_best_sequence(half1, symbol)
        sequence2 = get_best_sequence(half2, symbol)
        sequence = min(sequence1, sequence2)
        if sequence > 5:
            break

    if sequence == 10:
        print(f'ticket "{ticket}" - {sequence}{symbol} Jackpot!')
    elif sequence > 5:
        print(f'ticket "{ticket}" - {sequence}{symbol}')
    else:
        print(f'ticket "{ticket}" - no match')

# $$$$$$$$$$$$$$$$$$$$, aabb  , th@@@@@@eemo@@@@@@ey
