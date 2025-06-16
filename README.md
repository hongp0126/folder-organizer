# 🗂️ Folder Organizer

This is a simple desktop tool that helps you organize files in any folder by grouping them into categorized subfolders — such as Images, Documents, Videos, and more — based on their file extensions.

I made it mainly to keep my Downloads folder clean, but you can use it for any folder. It's built using Python and Tkinter, with a minimal dark mode interface.

---

## 🔧 Features

- Select any folder manually
- Automatically moves files into subfolders:
  - 📷 Images (`.png`, `.jpg`, etc.)
  - 📄 Documents (`.pdf`, `.txt`, etc.)
  - 🎬 Videos (`.mp4`, `.mkv`, etc.)
  - 📦 Compressed files (`.zip`, `.rar`, etc.)
  - 🧪 Executables, Logs, and everything else
- Simple UI with live summary
- Dark mode interface
- Supports `.exe` packaging (via PyInstaller)
- Optional custom icon

---

## ▶️ How to Run

### 1. Run via Python (if you have Python installed)

```bash
python folder_organizer.py
```

### 2. Or, run as an `.exe` file

If you've created a standalone `.exe`, just double-click to run it.  
(Tested on Windows 10+)

---

## 🛠️ Tech Stack

- Python 3
- Tkinter (GUI)
- Standard libraries: `os`, `shutil`, `collections`

---

## ❗ Notes

This script doesn't delete anything — it only moves files into subfolders.  
If you run it multiple times, it’ll just skip files already moved.

---

## 📌 Future ideas

Some features I'm considering for future updates:
- Custom categories (user-defined extension groups)
- Sort by creation/modification date
- Flatten subfolders
---

## 🧑‍💻 Author

Made by Hong Park.  
This was a side project to practice a bit of Python automation and GUI work. Feel free to fork or modify it if it's helpful.
