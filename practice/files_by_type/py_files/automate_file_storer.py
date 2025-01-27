import os, shutil

# Create a paths
actual_path = "./"
to_path = "../files_by_type/"

# List all files in the current directory
list_of_files = os.listdir(actual_path)

# Get the file type of each file in current directory
needed_directories = []
for file_type in list_of_files:
    file_name, type_of_file = file_type.split(".")
    if type_of_file not in needed_directories:
        needed_directories.append(type_of_file)

#Create directories:
for directory in needed_directories:
    os.mkdir(f"{to_path}/{directory}_files")

#move files by type to its corresponding directory

for file in list_of_files:
    file_name, ext = file.split(".")
    shutil.move(f"./{file}", f"{to_path}/{ext}_files/{file}")