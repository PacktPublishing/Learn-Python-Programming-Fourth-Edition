# json_examples/json_datetime.py
# Exercise: do the same for date
import json
from datetime import datetime, timedelta, timezone


now = datetime.now()
now_tz = datetime.now(tz=timezone(timedelta(hours=1)))


class DatetimeEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            try:
                off = obj.utcoffset().seconds
            except AttributeError:
                off = None

            return {
                "_meta": "datetime",
                "data": obj.timetuple()[:6] + (obj.microsecond,),
                "utcoffset": off,
            }
        return super().default(obj)


data = {
    "an_int": 42,
    "a_float": 3.14159265,
    "a_datetime": now,
    "a_datetime_tz": now_tz,
}

json_data = json.dumps(data, cls=DatetimeEncoder)

print(json_data)


def object_hook(obj):
    try:
        if obj["_meta"] == "datetime":
            if obj["utcoffset"] is None:
                tz = None
            else:
                tz = timezone(timedelta(seconds=obj["utcoffset"]))
            return datetime(*obj["data"], tzinfo=tz)
    except KeyError:
        return obj


data_out = json.loads(json_data, object_hook=object_hook)
print(data_out)

assert data_out["a_datetime"] == data["a_datetime"]
assert data_out["a_datetime_tz"] == data["a_datetime_tz"]


"""
$ python json_datetime.py

{
    "an_int": 42,
    "a_float": 3.14159265,
    "a_datetime": {
        "_meta": "datetime",
        "data": [2024, 3, 29, 23, 24, 22, 232302],
        "utcoffset": null,
    },
    "a_datetime_tz": {
        "_meta": "datetime",
        "data": [2024, 3, 30, 0, 24, 22, 232316],
        "utcoffset": 3600,
    },
}

{
    "an_int": 42,
    "a_float": 3.14159265,
    "a_datetime": datetime.datetime(
        2024, 3, 29, 23, 24, 22, 232302
    ),
    "a_datetime_tz": datetime.datetime(
        2024, 3, 30, 0, 24, 22, 232316,
        tzinfo=datetime.timezone(
            datetime.timedelta(seconds=3600)
        ),
    ),
}
"""
