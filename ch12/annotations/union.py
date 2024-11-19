# annotations/union.py
from typing import Union


def connect_to_database(host: str, port: Union[int, str]):
    print(f"Connecting to {host} on port {port}...")


def connect_to_db(host: str, port: int | str):
    print(f"Connecting to {host} on port {port}...")


if __name__ == "__main__":
    connect_to_database("localhost", 5432)
    connect_to_database("localhost", "5432")

    connect_to_db("localhost", 5432)
    connect_to_db("localhost", "5432")
