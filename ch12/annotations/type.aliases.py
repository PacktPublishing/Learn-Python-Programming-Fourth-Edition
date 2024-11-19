# annotations/type.aliases.py

type DatabasePort = int


def connect_to_database(host: str, port: DatabasePort):
    print(f"Connecting to {host} on port {port}...")


if __name__ == "__main__":
    connect_to_database("localhost", 5432)
