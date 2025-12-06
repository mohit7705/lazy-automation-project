"""
Create a ZIP backup of a folder INCLUDING subfolders.
Usage:
python backup_folder.py "C:/path/to/folder"
"""

import sys, zipfile, time
from pathlib import Path

def backup(folder):
    p = Path(folder)

    if not p.exists():
        print("Folder not found:", folder)
        return

    ts = time.strftime('%Y%m%d_%H%M%S')
    output_zip = p.parent / f"{p.name}_backup_{ts}.zip"

    with zipfile.ZipFile(output_zip, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for f in p.rglob('*'):
            zipf.write(f, arcname=f.relative_to(p.parent))

    print("Backup created at:", output_zip)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python backup_folder.py /path/to/folder")
    else:
        backup(sys.argv[1])
