# mypy_src/case.fixed.py
from collections.abc import Iterable


def title(names: Iterable[str | bytes]) -> list[str | bytes]:
    return [name.title() for name in names]


print(title(["ALICE", "bob"]))  # ['Alice', 'Bob'] - mypy OK
print(title([b"ALICE", b"bob"]))  # [b'Alice', b'Bob'] - mypy OK
