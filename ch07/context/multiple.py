# context/multiple.py
from decimal import Context, Decimal, localcontext


one = Decimal("1")
three = Decimal("3")

with (
    localcontext(Context(prec=5)),
    open("output.txt", "w") as out_file,
):
    out_file.write(f"{one} / {three} = {one / three}\n")

# Before Python 3.10 the above code would have to be written as:
# with localcontext(Context(prec=5)), \
#     open("output.txt", "w") as out_file:
#     out_file.write(f"{one} / {three} = {one / three}\n")
