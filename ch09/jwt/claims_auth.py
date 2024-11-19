# jwt/claims_auth.py
import jwt


data = {"payload": "data", "iss": "hein", "aud": "learn-python"}


secret = "secret-key"
token = jwt.encode(data, secret)


def decode(token, secret, issuer=None, audience=None):
    try:
        print(
            jwt.decode(
                token,
                secret,
                issuer=issuer,
                audience=audience,
                algorithms=["HS256"],
            )
        )
    except (
        jwt.InvalidIssuerError,
        jwt.InvalidAudienceError,
    ) as err:
        print(err)
        print(type(err))

# Not providing both the audience and issuer will fail
decode(token, secret)

# Not providing the issuer will succeed
decode(token, secret, audience="learn-python")

# Not providing the audience will fail
decode(token, secret, issuer="hein")

# Both will fail
decode(token, secret, issuer="wrong", audience="learn-python")
decode(token, secret, issuer="hein", audience="wrong")

# This will succeed
decode(token, secret, issuer="hein", audience="learn-python")


"""
$ python jwt/claims_time.py
Invalid audience
<class 'jwt.exceptions.InvalidAudienceError'>

{'payload': 'data', 'iss': 'hein', 'aud': 'learn-python'}

Invalid audience
<class 'jwt.exceptions.InvalidAudienceError'>

Invalid issuer
<class 'jwt.exceptions.InvalidIssuerError'>

Audience doesn't match
<class 'jwt.exceptions.InvalidAudienceError'>

{'payload': 'data', 'iss': 'hein', 'aud': 'learn-python'}

"""
