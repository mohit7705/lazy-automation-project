"""
Resize all images inside a folder INCLUDING subfolders.
Usage:
python resize_images.py "C:/path/to/folder" 800
"""

import sys
from pathlib import Path
from PIL import Image

def resize_folder(folder, max_size=1024):
    p = Path(folder)

    # Scan for images inside all subfolders
    images = [f for f in p.rglob('*') if f.is_file() and f.suffix.lower() in ('.jpg','.jpeg','.png','.bmp')]

    if not images:
        print("No images found to resize.")
        return

    for f in images:
        img = Image.open(f)
        img.thumbnail((int(max_size), int(max_size)))
        img.save(f)

    print(f"Resized {len(images)} images in {folder} (including subfolders).")

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print('Usage: python resize_images.py /path/to/folder max_size')
    else:
        resize_folder(sys.argv[1], int(sys.argv[2]))
