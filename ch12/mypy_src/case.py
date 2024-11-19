# mypy_src/case.py
from collections.abc import Iterable


def title(names: Iterable[str]) -> list[str]:
    return [name.title() for name in names]


print(title(["ALICE", "bob"]))  # ['Alice', 'Bob'] - mypy OK
print(title([b"ALICE", b"bob"]))  # [b'Alice', b'Bob'] - mypy ERR
