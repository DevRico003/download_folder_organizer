import os
import shutil
import time

# Define the folder to monitor and the folders to move files into
download_folder = os.path.expanduser("~/Downloads")
destination_folders = {
    'pdf': os.path.expanduser("~/Downloads/PDFs"),
    'jpg': os.path.expanduser("~/Downloads/JPGs"),
    'png': os.path.expanduser("~/Downloads/PNGs"),
    'mp3': os.path.expanduser("~/Downloads/Music"),
    'mp4': os.path.expanduser("~/Downloads/Videos"),
    'docx': os.path.expanduser("~/Downloads/Word"),
    'pptx': os.path.expanduser("~/Downloads/Powerpoint"),
    'exe': os.path.expanduser("~/Downloads/Programs"),
    'zip': os.path.expanduser("~/Downloads/Zips"),
    'MOV': os.path.expanduser("~/Downloads/Videos"),
    'xlsx': os.path.expanduser("~/Downloads/Excel"),
    'xls': os.path.expanduser("~/Downloads/Excel"),
    'ppt': os.path.expanduser("~/Downloads/Powerpoint"),
    'py': os.path.expanduser("~/Downloads/Python"),
    'sh': os.path.expanduser("~/Downloads/Bash"),
    'pem': os.path.expanduser("~/Downloads/SSH"),
    'ppk': os.path.expanduser("~/Downloads/SSH"),
    'csv': os.path.expanduser("~/Downloads/CSV"),
    'toml': os.path.expanduser("~/Downloads/TOML"),
    'json': os.path.expanduser("~/Downloads/JSON"),
    'txt': os.path.expanduser("~/Downloads/txt"),
    # Add other file types and destination folders here
}

# Create destination folders if they don't exist
for folder in destination_folders.values():
    if not os.path.exists(folder):
        os.makedirs(folder)

# Function to move files based on their extension
def move_file(file):
    filename, file_extension = os.path.splitext(file)
    file_extension = file_extension[1:]  # Remove the dot
    
    if file_extension in destination_folders:
        src_path = os.path.join(download_folder, file)
        dest_path = os.path.join(destination_folders[file_extension], file)
        
        shutil.move(src_path, dest_path)
        print(f"Moved {file} to {destination_folders[file_extension]}")

# Main loop to monitor the folder
while True:
    for filename in os.listdir(download_folder):
        if os.path.isfile(os.path.join(download_folder, filename)):
            move_file(filename)
    
    time.sleep(5)  # Wait for 5 seconds before checking again
