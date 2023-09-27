from decimal import localcontext, Decimal, ROUND_HALF_UP, ROUND_HALF_DOWN

with localcontext() as ctx:
    ctx.rounding = ROUND_HALF_UP
    for i in range(1, 15, 2):
        n = Decimal(i) / 2
        print(n, '=>', n.to_integral_value(), end='   ')

print(':\n:\n:\n')

with localcontext() as ctx:
    ctx.rounding = ROUND_HALF_DOWN
    for i in range(1, 15, 2):
        n = Decimal(i) / 2
        print(n, '=>', n.to_integral_value())
