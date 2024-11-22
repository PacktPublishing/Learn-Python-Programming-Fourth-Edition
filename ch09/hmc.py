# hmc.py
import hmac
import hashlib


def calc_digest(key, message):
    key = bytes(key, "utf-8")
    message = bytes(message, "utf-8")

    dig = hmac.new(key, message, hashlib.sha256)
    return dig.hexdigest()


mac = calc_digest("secret-key", "Important Message")
print(mac)
# 1db5d806d73d76e779b7fd31091e026362a64177368e82e0cab91e0c2fb6435e
