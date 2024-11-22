# jwt/claims_time.py
from datetime import datetime, timedelta, UTC
from time import sleep, time

import jwt


iat = datetime.now(tz=UTC)
nfb = iat + timedelta(seconds=1)
exp = iat + timedelta(seconds=3)


data = {"payload": "data", "nbf": nfb, "exp": exp, "iat": iat}


def decode(token, secret):
    print(f"{time():.2f}")
    try:
        print(jwt.decode(token, secret, algorithms=["HS256"]))
    except (
        jwt.ImmatureSignatureError,
        jwt.ExpiredSignatureError,
    ) as err:
        print(err)
        print(type(err))


secret = "secret-key"
token = jwt.encode(data, secret)


decode(token, secret)
sleep(2)
decode(token, secret)
sleep(2)
decode(token, secret)


"""
$ python jwt/claims_time.py
1716674892.39
The token is not yet valid (nbf)
<class 'jwt.exceptions.ImmatureSignatureError'>

1716674894.39
{'payload': 'data', 'nbf': 1716674893, 'exp': 1716674895, 'iat': 1716674892}

1716674896.39
Signature has expired
<class 'jwt.exceptions.ExpiredSignatureError'>
"""
