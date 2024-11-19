# secrs/secr_rand.py
import secrets


# Utils
print(secrets.choice("Choose one of these words".split()))

print(secrets.randbelow(10**6))

print(secrets.randbits(32))


# Tokens
print(secrets.token_bytes(16))

print(secrets.token_hex(32))

print(secrets.token_urlsafe(32))

# Compare digests against timing attacks
secrets.compare_digest("abc123", "abc123")

"""
$ python secr_rand.py
one
133025
1509555468
b'\x0f\x8b\x8f\x0f\xe3\xceJ\xbc\x18\xf2\x1e\xe0i\xee1\x99'
98e80cddf6c371811318045672399b0950b8e3207d18b50d99d724d31d17f0a7
63eNkRalj8dgZqmkezjbEYoGddVcutgvwJthSLf5kho
"""
