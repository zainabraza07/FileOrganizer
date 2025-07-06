import os
import shutil

def organize(folder_path):
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        if os.path.isfile(file_path):
            ext = filename.split('.')[-1].upper() + "_Files"
            new_folder = os.path.join(folder_path, ext)
            os.makedirs(new_folder, exist_ok=True)
            shutil.move(file_path, os.path.join(new_folder, filename))

# Example usage
folder = input("Enter full folder path to organize: ")
organize(folder)
print("Files organized by type!")
