import os
import shutil

# Take folder path from user
path = input("Enter folder path: ")

# Check if path exists
if not os.path.exists(path):
    print("Invalid path!")
    exit()

files = os.listdir(path)

for file in files:
    file_path = os.path.join(path, file)

    # Skip folders
    if os.path.isdir(file_path):
        continue

    filename, extension = os.path.splitext(file)

    extension = extension.lower()

    # Categorize files
    if extension in [".jpg", ".png", ".jpeg"]:
        folder = "Images"
    elif extension in [".pdf", ".docx", ".txt"]:
        folder = "Documents"
    elif extension in [".mp4", ".mkv"]:
        folder = "Videos"
    elif extension in [".mp3"]:
        folder = "Music"
    else:
        folder = "Others"

    folder_path = os.path.join(path, folder)

    # Create folder if not exists
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    destination = os.path.join(folder_path, file)

    # Handle duplicate files
    count = 1
    while os.path.exists(destination):
        new_name = f"{filename}_{count}{extension}"
        destination = os.path.join(folder_path, new_name)
        count += 1

    # Move file
    shutil.move(file_path, destination)

    print(f"Moved: {file} → {folder}")

print("✅ All files organized successfully!")
