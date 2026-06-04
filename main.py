import os
import shutil

folder_path = r"C:\Users\user\Downloads"

for filename in os.listdir(folder_path):
    file_path = os.path.join(folder_path, filename)

    if os.path.isfile(file_path):
        extension = filename.split(".")[-1]

        destination_folder = os.path.join(folder_path, extension.upper())

        if not os.path.exists(destination_folder):
            os.makedirs(destination_folder)

        shutil.move(file_path, os.path.join(destination_folder, filename))

print("Files Organized Successfully!")