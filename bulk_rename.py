"""
Bulk rename files in a folder (including subfolders) with a prefix.
Usage:
python bulk_rename.py "C:/path/to/folder" IMG
"""

import sys
from pathlib import Path

def bulk_rename(folder, prefix='file'):
    p = Path(folder)

    # Collect all files inside folder & subfolders
    files = sorted([f for f in p.rglob('*') if f.is_file()])
    
    if not files:
        print("No files found to rename.")
        return

    width = len(str(len(files)))

    for i, f in enumerate(files, start=1):
        ext = f.suffix
        new_name = f"{prefix}_{str(i).zfill(width)}{ext}"
        f.rename(f.with_name(new_name))

    print(f"Renamed {len(files)} files inside {folder} (including subfolders).")

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print('Usage: python bulk_rename.py "path/to/folder" prefix')
    else:
        bulk_rename(sys.argv[1], sys.argv[2])
