# Downloads Folder File Organizer

A simple Python automation script that organizes files in your **Downloads** folder by moving them into appropriate folders like Documents, Pictures, Archives, and Videos based on their extensions.



##  How It Works

- Uses `os` and `shutil` modules from Python standard library.
- Categorizes files based on extension types.
- Moves files to:
  - `.pdf`, `.txt`, etc → Documents
  - `.jpg`, `.png`, etc → Pictures
  - `.zip`, `.tar.gz`, etc → Archives
  - `.mp4`, `.mkv`, etc → Videos
- Automatically skips folders and unsupported extensions.


---

## 🛠 Requirements

- Python 3.x  
- Works on **Linux** (tested on Lubuntu)
- No external libraries needed

---

##  How to Use

1. Make sure your **Downloads** folder contains mixed files.
2. Run the script:

```bash
python3 file_organiser.py

##  Safety 

Skips directories
Creates target folders if they don't exist
Handles .tar.gz, .tgz, and compound extensions properly
Uses decorators for logging (just for learning)

## ABOUT ME:
Kushagra Saini
📍 B.Tech CSE (Cloud Computing & Automation), Vellore Institute of Technology (Bhopal)
🔭 Career Goals: DevOps, System Design, Platform Engineering
💻 Passionate about automation and solving real-world problems with Python.
