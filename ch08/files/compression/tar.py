# files/compression/tar.py
import tarfile

with tarfile.open("example.tar.gz", "w:gz") as tar:
    tar.add("content1.txt")
    tar.add("content2.txt")
    tar.add("subfolder/content3.txt")
    tar.add("subfolder/content4.txt")

with tarfile.open("example.tar.gz", "r:gz") as tar:
    tar.extractall("extract_tar", filter="data")


"""
SECURITY NOTE:

The code in this module is for illustration purposes only.
For the sake of simplicity, the code does not validate the file paths.
It is not secure to extract files from an archive without validating the file paths.

Please see:

- https://docs.python.org/3/library/tarfile.html#tarfile.TarFile.extractall
- https://github.com/advisories/GHSA-gw9q-c7gh-j9vm

for more information.
"""
