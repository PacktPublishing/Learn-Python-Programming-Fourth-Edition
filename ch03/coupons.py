# coupons.py
customers = [
    dict(id=1, total=200, coupon_code="F20"),  # F20: fixed, £20
    dict(id=2, total=150, coupon_code="P30"),  # P30: percent, 30%
    dict(id=3, total=100, coupon_code="P50"),  # P50: percent, 50%
    dict(id=4, total=110, coupon_code="F15"),  # F15: fixed, £15
]
for customer in customers:
    match customer["coupon_code"]:
        case "F20":
            customer["discount"] = 20.0
        case "F15":
            customer["discount"] = 15.0
        case "P30":
            customer["discount"] = customer["total"] * 0.3
        case "P50":
            customer["discount"] = customer["total"] * 0.5
        case _:
            customer["discount"] = 0.0

for customer in customers:
    print(customer["id"], customer["total"], customer["discount"])
