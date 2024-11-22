# files/existence.py
from pathlib import Path

p = Path("fear.txt")
path = p.parent.absolute()

print(p.is_file())  # True
print(path)  # /Users/fab/code/lpp4ed/ch08/files
print(path.is_dir())  # True

q = Path("/Users/fab/code/lpp4ed/ch08/files")
print(q.is_dir())  # True
