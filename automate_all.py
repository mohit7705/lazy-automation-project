"""
Run ALL automations in one go:
1. Organize files
2. Bulk rename (works in subfolders)
3. Resize images
4. Remove duplicate files
5. Summarize text files
6. Create backup ZIP

Usage:
python automate_all.py "C:/path/to/folder" PREFIX 800
Example:
python automate_all.py "C:/Users/rajpu/Downloads/test_folder" IMG 800
"""

import sys
from pathlib import Path
import subprocess

def run_script(script, *args):
    cmd = ["python", script] + list(args)
    print("\n===============================")
    print("Running:", " ".join(cmd))
    print("===============================\n")
    subprocess.run(cmd)

if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("Usage: python automate_all.py <folder_path> <prefix> <max_size>")
        print("Example: python automate_all.py \"C:/folder\" IMG 800")
        sys.exit()

    folder = sys.argv[1]
    prefix = sys.argv[2]
    max_size = sys.argv[3]

    # 1. Organize files
    run_script("organize_files.py", folder)

    # 2. Bulk rename
    run_script("bulk_rename.py", folder, prefix)

    # 3. Resize images
    run_script("resize_images.py", folder, max_size)

    # 4. Remove duplicates
    run_script("remove_duplicates.py", folder)

    # 5. Summarize text files
    run_script("summarize_texts.py", folder)

    # 6. Create backup ZIP
    run_script("backup_folder.py", folder)

    print("\n🎉 All tasks completed successfully!")
