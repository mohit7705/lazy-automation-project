"""
Detect and optionally delete duplicate files inside a folder INCLUDING subfolders.
Usage:
python remove_duplicates.py "C:/path/to/folder"
python remove_duplicates.py "C:/path/to/folder" --delete
"""

import sys, hashlib
from pathlib import Path

def hash_file(path, block_size=65536):
    h = hashlib.sha256()
    with open(path, 'rb') as f:
        for block in iter(lambda: f.read(block_size), b''):
            h.update(block)
    return h.hexdigest()

def find_duplicates(folder, delete=False):
    p = Path(folder)

    # Scan all files in folder + subfolders
    files = [f for f in p.rglob('*') if f.is_file()]
    hashes = {}
    duplicates = []

    for f in files:
        file_hash = hash_file(f)
        if file_hash in hashes:
            duplicates.append((f, hashes[file_hash]))
        else:
            hashes[file_hash] = f

    # Delete duplicates if requested
    if delete:
        for dup, original in duplicates:
            print("Deleting duplicate:", dup)
            dup.unlink()

    print(f"Found {len(duplicates)} duplicates in {folder}.")
    return duplicates

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python remove_duplicates.py /path/to/folder [--delete]")
    else:
        delete_flag = "--delete" in sys.argv
        find_duplicates(sys.argv[1], delete_flag)
