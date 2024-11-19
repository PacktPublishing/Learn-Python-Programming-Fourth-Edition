# files/walking.pathlib.py
from pathlib import Path


p = Path(".")

for root, dirs, files in p.walk():
    print(f"{root=}")

    if dirs:
        print("Directories:")
        for dir_ in dirs:
            print(dir_)
        print()

    if files:
        print("Files:")
        for filename in files:
            print(filename)
        print()


"""
$ python walking.pathlib.py
root=PosixPath('.')
Directories:
compression

Files:
existence.py
manipulation.py
print_file.py
read_write_bin.py
paths.py
open_with.py
walking.py
tmp.py
read_write.py
listing.py
write_not_exists.py
ops_create.py
fear.txt
open_try.py
walking.pathlib.py

root=PosixPath('compression')
Directories:
subfolder

Files:
tar.py
content1.txt
content2.txt
zip.py

root=PosixPath('compression/subfolder')
Files:
content3.txt
content4.txt
"""
