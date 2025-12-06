# lazy-automation-project
🌟 Overview

This project automates six common digital tasks using simple Python scripts.
You can use these scripts to quickly organize files, rename them, resize images, remove duplicates, summarize text files, and create backups.

The goal of this project is to save time by removing boring manual work.

🧩 Features (6 Automation Scripts)
1️⃣ Organize Files

Sorts files into folders based on their extensions (.jpg, .png, .pdf, etc.)

python organize_files.py "folder_path"

2️⃣ Bulk Rename Files (supports subfolders)

Renames all files in the folder and inside subfolders using a prefix like IMG, FILE, etc.

python bulk_rename.py "folder_path" IMG

3️⃣ Resize Images (supports subfolders)

Resizes all images to a given maximum size.

python resize_images.py "folder_path" 800

4️⃣ Remove Duplicate Files

Finds duplicate files by checking file content using hashing.

Check duplicates:

python remove_duplicates.py "folder_path"


Delete duplicates:

python remove_duplicates.py "folder_path" --delete

5️⃣ Summarize Text Files

Summarizes all .txt files inside the folder and subfolders.

python summarize_texts.py "folder_path"

6️⃣ Backup the Folder

Creates a .zip backup of the entire folder (including subfolders).

python backup_folder.py "folder_path"

📁 Folder Structure Example
lazy-automation-project/
│── organize_files.py
│── bulk_rename.py
│── resize_images.py
│── remove_duplicates.py
│── summarize_texts.py
│── backup_folder.py
│── requirements.txt
│── README.md
└── .kiro/
       └── kiro-config.json

⚙️ Installation
Step 1: Install required libraries

Inside VS Code terminal:

pip install -r requirements.txt

Step 2: Install NLTK data

Open Python shell:

import nltk
nltk.download('punkt')

🧪 Testing the Project

You can test the scripts using a real folder that contains:

Images

PDFs

Text files

Duplicate files

Example test command:

python organize_files.py "C:\Users\YourName\Downloads\test_folder"

📝 Purpose of the Project

This project was created for the Kiro Week 2 Challenge (Lazy Automation) to demonstrate:

File automation

Folder management

Python scripting

Problem-solving

Using Kiro to speed up development

🤝 Contributing

This is a simple educational project.
Feel free to fork it and add more automation features!

📄 License

This project is free to use for learning purposes.
