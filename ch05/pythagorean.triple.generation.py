# pythagorean.triple.generation.py
from functions import gcd


N = 50

triples = sorted(  # 1
    (
        (a, b, c)
        for a, b, c in (  # 2
            ((m**2 - n**2), (2 * m * n), (m**2 + n**2))  # 3
            for m in range(1, int(N**0.5) + 1)  # 4
            for n in range(1, m)  # 5
            if (m - n) % 2 and gcd(m, n) == 1  # 6
        )
        if c <= N  # 7
    ),
    key=sum,  # 8
)


print(triples)
