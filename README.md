# File Synchronizer Script
Simple Python script that updates specified files from source folder to destination folder.

# Overview
A Python script to synchronize files between two directories based on file extensions and names.

This script is designed to copy files from a source directory to a destination directory, while also updating existing files if they have changed. The script uses file hashes to compare files and only updates files that have changed.

# Features
- Copies files from a source directory to a destination directory based on file extensions
- Updates existing files if they have changed
- Skips files that start with a specified prefix
- Logs all file operations to a log file

# Tips
- Run this script in a schedule using:
  Crontab (Linux)
  Task scheduler (Windows)

# Requirements
- Python 3.x
- os, hashlib, shutil, and datetime modules (included with Python)

# Configuration
The script uses the following variables to configure its behavior:

- source_folder: The source directory to copy files from
- destination_folder: The destination directory to copy files to
- name_filter: The prefix to filter files by (e.g., "TEXTFILE_") LEAVE THIS "" OR "*"
- skip_logging: The prefix to skip logging for (e.g., "SKIP_") LEAVE THIS "" OR "*"
- extension: The file extensions to copy (e.g., ".xls", ".txt", ".pdf")
- logging_file: The log file to write to (Script writes a line per file changed with action and time data)

# Usage
1. Clone the repository to your local machine
2. Configure the script by modifying the variables at the top of the script
3. Run the script using Python (e.g., file_sync.py)

# Devs
- rowletontop
  
# License
This project is licensed under the MIT License. See the LICENSE file for details.
