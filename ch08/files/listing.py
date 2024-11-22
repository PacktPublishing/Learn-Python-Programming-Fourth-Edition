# files/listing.py
from pathlib import Path


p = Path(".")

for entry in p.glob("*"):
    print("File:" if entry.is_file() else "Folder:", entry)


"""
$ python listing.py
File: existence.py
File: manipulation.py
File: print_file.py
File: read_write_bin.py
File: paths.py
File: open_with.py
File: walking.py
File: tmp.py
File: read_write.py
File: listing.py
File: write_not_exists.py
Folder: compression
File: ops_create.py
File: fear.txt
File: open_try.py
File: walking.pathlib.py
"""
