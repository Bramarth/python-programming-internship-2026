
import os
import shutil

# Map file extensions to their categories
FILE_CATEGORIES = {
    # Documents
    ".pdf": "Documents",
    ".doc": "Documents",
    ".docx": "Documents",
    ".txt": "Documents",
    ".ppt": "Documents",
    ".pptx": "Documents",
    ".xls": "Documents",
    ".xlsx": "Documents",
    ".csv": "Documents",

    # Images
    ".jpg": "Images",
    ".jpeg": "Images",
    ".png": "Images",
    ".gif": "Images",
    ".bmp": "Images",
    ".svg": "Images",

    # Videos
    ".mp4": "Videos",
    ".mkv": "Videos",
    ".avi": "Videos",
    ".mov": "Videos",
    ".wmv": "Videos",

    # Archives
    ".zip": "Archives",
    ".rar": "Archives",
    ".7z": "Archives",
    ".tar": "Archives",
    ".gz": "Archives",

    # Code
    ".py": "Code",
    ".java": "Code",
    ".html": "Code",
    ".css": "Code",
    ".js": "Code",
    ".cpp": "Code",
    ".c": "Code",
    ".php": "Code"
}


def get_unique_destination(destination):
    """Generate a unique filename if the destination already exists."""
    folder = os.path.dirname(destination)
    filename = os.path.basename(destination)
    name, extension = os.path.splitext(filename)

    counter = 1

    while os.path.lexists(destination):
        new_filename = f"{name}_{counter}{extension}"
        destination = os.path.join(folder, new_filename)
        counter += 1

    return destination


def organize_files():
    """Scan a directory and move files into category folders."""

    folder_path = input("Enter the folder path to organize: ").strip()
    folder_path = os.path.expanduser(folder_path)

    if not os.path.isdir(folder_path):
        print("\nError: The specified folder does not exist.")
        return

    print("\n========== FILE ORGANIZER ==========")
    print(f"Scanning: {folder_path}\n")

    moved = 0
    failed = 0

    try:
        with os.scandir(folder_path) as entries:
            for entry in entries:

                # Only process regular files, not directories
                if not entry.is_file(follow_symlinks=False):
                    continue

                filename = entry.name
                extension = os.path.splitext(filename)[1].lower()

                # Identify the appropriate category
                category = FILE_CATEGORIES.get(extension, "Others")

                # Create the category folder if necessary
                category_folder = os.path.join(folder_path, category)

                try:
                    os.makedirs(category_folder, exist_ok=True)

                    # Determine the destination
                    destination = os.path.join(
                        category_folder, filename
                    )

                    # Avoid overwriting existing files
                    destination = get_unique_destination(destination)

                    # Move the file
                    shutil.move(entry.path, destination)

                    print(f"[MOVED] {filename} -> {category}/")
                    moved += 1

                except PermissionError:
                    print(f"[DENIED] Permission denied: {filename}")
                    failed += 1

                except (shutil.Error, OSError) as error:
                    print(f"[ERROR] Could not move {filename}: {error}")
                    failed += 1

    except PermissionError:
        print("Error: You do not have permission to access this folder.")
        return

    except OSError as error:
        print(f"Error while scanning folder: {error}")
        return

    # Display execution summary
    print("\n========== EXECUTION SUMMARY ==========")
    print(f"Files successfully moved: {moved}")
    print(f"Files that could not be moved: {failed}")
    print("Organization process completed.")


if __name__ == "__main__":
    organize_files()
