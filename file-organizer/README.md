# Automated File Organizer

A Python-based desktop file organization utility developed during the Datheon Engineering Cohort 2026. The program automatically scans a selected directory, identifies files by their extensions, creates category folders, and moves files into their appropriate locations.

## Features

- Scans a user-selected directory using Python's OS library.
- Identifies file types based on their extensions.
- Automatically creates category folders.
- Organizes files into Documents, Images, Videos, Archives, Code, and Others.
- Moves files using Python's shutil library.
- Prevents existing files from being overwritten by generating unique filenames.
- Handles permission errors and file movement exceptions.
- Displays an execution summary showing successfully moved and failed files.

## File Categories

| Category | Supported File Types |
|---|---|
| Documents | PDF, DOC, DOCX, TXT, PPT, PPTX, XLS, XLSX, CSV |
| Images | JPG, JPEG, PNG, GIF, BMP, SVG |
| Videos | MP4, MKV, AVI, MOV, WMV |
| Archives | ZIP, RAR, 7Z, TAR, GZ |
| Code | PY, JAVA, HTML, CSS, JS, CPP, C, PHP |
| Others | Unrecognised file types |

## Technologies Used

- Python 3
- OS module
- Shutil module

## How to Run

1. Install Python 3.
2. Download or clone this repository.
3. Navigate to the File-Organizer directory.
4. Run the program:

```bash
python organizer.py
```

5. Enter the path of the directory you want to organize when prompted.

## Example Output

```text
========== FILE ORGANIZER ==========
Scanning: C:\Users\YourName\Downloads\TestFolder

[MOVED] report.pdf -> Documents/
[MOVED] photo.jpg -> Images/
[MOVED] program.py -> Code/

========== EXECUTION SUMMARY ==========
Files successfully moved: 3
Files that could not be moved: 0
Organization process completed.
```

## Important Note

The program moves files from the selected directory into category folders rather than copying them. It is recommended to test the utility using a sample directory before organizing important files.

## Author
Developed as part of the Datheon Engineering Cohort 2026 Python Programming Internship.

Developed as part of the Datheon Engineering Cohort 2026 Python Programming Internship.
