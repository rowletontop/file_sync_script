import os
import hashlib
import shutil
import datetime

# Variables
source_folder = r"C:\Temp\Source-test" 
destiny_folder = r"C:\Temp\Destination-test"
name_filter = "" #Keep this to "" or "*" to ignore the namefilter  # The start of a file it should look for (f.e. TEXTFILE_ to make it look for files that start with TEXTFILE_)
skip_logging = "" #Keep this to "" or "*" to ignore the namefilter # Files which it will ignore logging, please use a wildcard.
extension = (".example", ".txt", ".extension") # The file extensions it will look for
logging_file = r"C:\Temp\log.txt" # Output file for the loggies

def get_file_hash(file_path):
    with open(file_path, 'rb') as file:
        file_hash = hashlib.sha1(file.read()).hexdigest()
    return file_hash

source_files = [
    os.path.join(root, file)
    for root, dirs, files in os.walk(source_folder)
    for file in files if file.startswith(name_filter) and file.endswith(extension)
]

destiny_files = [
    os.path.join(root, file)
    for root, dirs, files in os.walk(destiny_folder)
    for file in files if file.endswith(extension)
]

# If no source files are found
if not source_files:
    print(f"No files found within {source_folder} that end with extension: {extension}.")
else:
    print(f"There are: {len(source_files)} files found with: {extension}.")

# If no destination files are found
if not destiny_files:
    print(f"No files found in {destiny_folder}. Cannot compare files. Matching files will get updated.")
    for file in source_files:
        file_name = os.path.basename(file)
        copy_destination = os.path.join(destiny_folder, file_name)
        try:
            shutil.copy2(file, copy_destination)
            print(f"File {file_name} copied.")
            with open(logging_file, 'a') as log_file:
                log_file.write(f"File {file} is copied. {datetime.datetime.now().strftime('%Y-%m-%d | %H:%M:%S')}\n")
        except Exception as e:
            print(f"Error! File can't be copied. reason: {file_name}: {str(e)}")
            with open(logging_file, 'a') as log_file:
                log_file.write(f"ERROR File {file} not copied {datetime.datetime.now().strftime('%Y-%m-%d | %H:%M:%S')} {str(e)}\n")

else:
    # This is the comparing part of the script --->
    source_files_set = set(os.path.basename(file) for file in source_files)
    destiny_files_set = set(os.path.basename(file) for file in destiny_files)
    new_files = source_files_set - destiny_files_set
    for file in new_files:
        file_path = next((file_path for file_path in source_files if os.path.basename(file_path) == file), None)
        copy_destination = os.path.join(destiny_folder, file)
        try:
            shutil.copy2(file_path, copy_destination)
            print(f"File {file} copied.")
            with open(logging_file, 'a') as log_file:
                log_file.write(f"File {file} is copied. {datetime.datetime.now().strftime('%Y-%m-%d | %H:%M:%S')}\n")
        except Exception as e:
            print(f"Error! File can't be copied. reason: {file}: {str(e)}")
            with open(logging_file, 'a') as log_file:
                log_file.write(f"ERROR File {file} not copied {datetime.datetime.now().strftime('%Y-%m-%d | %H:%M:%S')} {str(e)}\n")
    # update existing files if changed from the original one
    existing_files = source_files_set & destiny_files_set
    for file in existing_files:
        source_file_path = next((file_path for file_path in source_files if os.path.basename(file_path) == file), None)
        destiny_file_path = next((file_path for file_path in destiny_files if os.path.basename(file_path) == file), None)

        if get_file_hash(source_file_path) != get_file_hash(destiny_file_path):
            try:
                shutil.copy2(source_file_path, destiny_file_path)
                print(f"File {file} updated.")
                with open(logging_file, 'a') as log_file:
                    log_file.write(f"File {file} is updated. {datetime.datetime.now().strftime('%Y-%m-%d | %H:%M:%S')}\n")
            except Exception as e:
                print(f"Error! File can't be updated, because: {file}: {str(e)}")
                with open(logging_file, 'a') as log_file:
                    log_file.write(f"ERROR file {file} not updated! {datetime.datetime.now().strftime('%Y-%m-%d | %H:%M:%S')} {str(e)}\n")

skipped_files = [
    os.path.join(root, file)
    for root, dirs, files in os.walk(source_folder)
    for file in files if file.endswith(extension) and file.startswith(skip_logging)
]

for file in skipped_files:
    print(f"File {file} skipped: File starts with {skip_logging}.")
