"""Organize files in a folder by extension into subfolders.
Usage: python organize_files.py /path/to/folder
"""
import sys
from pathlib import Path

def organize(folder):
    p = Path(folder)
    if not p.exists():
        print('Folder does not exist:', folder)
        return
    for f in p.iterdir():
        if f.is_file():
            ext = f.suffix.lower().strip('.') or 'no_ext'
            dest = p / ext
            dest.mkdir(exist_ok=True)
            f.rename(dest / f.name)
    print('Organized', folder)

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Usage: python organize_files.py /path/to/folder')
    else:
        organize(sys.argv[1])
