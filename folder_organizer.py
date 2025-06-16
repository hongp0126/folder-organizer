import os # Provides OS-level functions like path and file checks
import shutil # Allows file movement and copying
from tkinter import Tk, Label, Button, filedialog, Text, END
from collections import defaultdict

# File categories by extension
file_categories = {
    'Images': ['.png', '.jpg', '.jpeg', '.gif'],
    'Documents': ['.pdf', '.docx', '.txt'],
    'Executables': ['.exe', '.msi'],
    'Compressed': ['.zip', '.rar', '.7z', '.gz'],
    'Videos': ['.mp4', '.mkv', '.avi'],
    'Logs': ['.log'],
    'Others': []
}

def organize_files():
    folder_path = filedialog.askdirectory() # Ask the user to select a folder
    if not folder_path: # Exit if no folder is selected
        return

    # Dictionary to track number of files moved per category
    summary = defaultdict(int)

    # Iterate through all items in the selected folder
    for file in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file)
        
        # Skip if it's not a file
        if os.path.isfile(file_path):
            ext = os.path.splitext(file)[1].lower() # Extract file extension (case-insensitive)
            moved = False
            
            # Check each category and move file if it matches an extension
            for category, extensions in file_categories.items(): 
                if ext in extensions:
                    dest_folder = os.path.join(folder_path, category)
                    os.makedirs(dest_folder, exist_ok=True) 
                    shutil.move(file_path, os.path.join(dest_folder, file)) # Allows the file to move to the destination folder
                    summary[category] += 1
                    moved = True
                    break
            # If no category matched, move to 'Others'
            if not moved:
                others_folder = os.path.join(folder_path, 'Others')
                os.makedirs(others_folder, exist_ok=True)
                shutil.move(file_path, os.path.join(others_folder, file))
                summary['Others'] += 1
                
    # Display result summary
    result_box.delete(1.0, END)
    total = sum(summary.values())
    result_box.insert(END, f"✅ Total files organized: {total}\n")

    for category, count in summary.items():
        result_box.insert(END, f"- {category}: {count} moved\n")
        
# Setup GUI
root = Tk()
root.title("Folder Organizer")
root.geometry("400x300")

root.configure(bg="#2E2E2E")  # Dark mode background

# UI elements
label = Label(root, text="📂 Please select a folder to organize", font=("Arial", 12), bg="#2E2E2E", fg="white")
label.pack(pady=10)

btn = Button(root, text="Select a folder", command=organize_files, bg="#444444", fg="white", activebackground="#666666")
btn.pack(pady=5)

result_box = Text(root, height=10, width=50, bg="#1E1E1E", fg="white", insertbackground="white")
result_box.pack(pady=10)

root.mainloop() # Start GUI event loop