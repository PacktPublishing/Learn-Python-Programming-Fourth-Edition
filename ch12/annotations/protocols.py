# annotations/protocols.py
from typing import Iterable, Protocol


class SupportsStart(Protocol):
    def start(self) -> None: ...


class Worker:  # No SupportsStart base class.
    def __init__(self, name: str) -> None:
        self.name = name

    def start(self) -> None:
        print(f"Starting worker {self.name}")


def start_workers(workers: Iterable[SupportsStart]) -> None:
    for worker in workers:
        worker.start()


workers = [Worker("Alice"), Worker("Bob")]
start_workers(workers)
# Starting worker Alice
# Starting worker Bob
