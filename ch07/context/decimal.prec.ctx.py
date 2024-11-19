# context/decimal.prec.ctx.py
from decimal import Context, Decimal, localcontext


one = Decimal("1")
three = Decimal("3")

with localcontext(Context(prec=5)) as ctx:
    print("Custom decimal context:", one / three)

print("Original context restored:", one / three)
