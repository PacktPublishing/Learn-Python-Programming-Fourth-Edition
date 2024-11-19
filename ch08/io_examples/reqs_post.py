# io_examples/reqs_post.py
import requests


url = "https://httpbin.org/post"
data = dict(title="Learn Python Programming")


resp = requests.post(url, data=data)
print("Response for POST")
print(resp.json())


"""
$ python reqs_post.py

Response for POST
{
    "args": {},
    "data": "",
    "files": {},
    "form": {"title": "Learn Python Programming"},
    "headers": {
        "Accept": "*/*",
        "Accept-Encoding": "gzip, deflate",
        "Content-Length": "30",
        "Content-Type": "application/x-www-form-urlencoded",
        "Host": "httpbin.org",
        "User-Agent": "python-requests/2.31.0",
        "X-Amzn-Trace-Id": "Root=1-123abc-123abc",
    },
    "json": None,
    "origin": "86.14.44.233",
    "url": "https://httpbin.org/post",
}
"""
