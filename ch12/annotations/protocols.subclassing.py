# annotations/protocols.subclassing.py
from typing import Iterable, Protocol


class SupportsStart(Protocol):
    def start(self) -> None: ...


class SupportsStop(Protocol):
    def stop(self) -> None: ...


class SupportsWorkCycle(SupportsStart, SupportsStop, Protocol):
    pass


class Worker:
    def __init__(self, name: str) -> None:
        self.name = name

    def start(self) -> None:
        print(f"Starting worker {self.name}")

    def stop(self) -> None:
        print(f"Stopping worker {self.name}")


def start_workers(workers: Iterable[SupportsWorkCycle]) -> None:
    for worker in workers:
        worker.start()
        worker.stop()


workers = [Worker("Alice"), Worker("Bob")]
start_workers(workers)
# Starting worker Alice
# Stopping worker Alice
# Starting worker Bob
# Stopping worker Bob
