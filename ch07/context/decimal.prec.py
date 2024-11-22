# context/decimal.prec.py
from decimal import Context, Decimal, getcontext, setcontext

one = Decimal("1")
three = Decimal("3")

orig_ctx = getcontext()
ctx = Context(prec=5)
setcontext(ctx)
print(f"{ctx}\n")

print("Custom decimal context:", one / three)
setcontext(orig_ctx)
print("Original context restored:", one / three)


"""
Context(prec=5, rounding=ROUND_HALF_EVEN, Emin=-999999,
        Emax=999999, capitals=1, clamp=0, flags=[],
        traps=[InvalidOperation, DivisionByZero, Overflow])

Custom decimal context: 0.33333
Original context restored: 0.3333333333333333333333333333
"""
