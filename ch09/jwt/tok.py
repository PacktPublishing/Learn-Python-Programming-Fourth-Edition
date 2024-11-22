# jwt/tok.py
import jwt


data = {"payload": "data", "id": 123456789}
algs = ["HS256", "HS512"]

token = jwt.encode(data, "secret-key")
data_out = jwt.decode(token, "secret-key", algorithms=algs)
print(token)
print(data_out)


# Decode without verifying the signature
jwt.decode(token, options={"verify_signature": False})


# Let's use another algorithm
token512 = jwt.encode(data, "secret-key", algorithm="HS512")
data_out = jwt.decode(
    token512, "secret-key", algorithms=["HS512"]
)
print(data_out)

"""
$ python jwt/tok.py
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJwYXlsb2FkIjoiZGF0YSIsIm...
{'payload': 'data', 'id': 123456789}
{'payload': 'data', 'id': 123456789}
"""
