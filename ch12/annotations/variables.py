x: int = 10
x: float = 3.14
x: bool = True
x: str = "Hello!"
x: bytes = b"Hello!"

# Python 3.9+
x: list[int] = [7, 14, 21]
x: set[int] = {1, 2, 3}
x: dict[str, float] = {"planck": 6.62607015e-34}

x: tuple[int, str, float] = (1, "on", 2.8)
x: tuple[int, ...] = (1, 2, 3)

# Python 3.8 and earlier
from typing import List, Set, Dict, Tuple

x: List[int] = [7, 14, 21]
x: Set[int] = {1, 2, 3}
x: Dict[str, float] = {"planck": 6.62607015e-34}

x: Tuple[int, str, float] = (1, "on", 2.8)
x: Tuple[int, ...] = (1, 2, 3)

# Python 3.10+
x: list[int | str] = [0, 1, 1, 2, "fibonacci", "rules"]

# Python 3.9 and earlier
from typing import Union

x: list[Union[int, str]] = [0, 1, 1, 2, "fibonacci", "rules"]
