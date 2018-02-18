# general imports
import os

# this function returns the current size of a folder
def get_folder_size(path):
    s = 0.0

    for entry in os.scandir(path):
        if entry.is_file():
            s += entry.stat().st_size / 1024000 # transform from bynary bytes to decimal megabytes

        elif entry.is_dir():
            s += get_folder_size(path + "/" + entry.name)

    return s

# this function returns the size of a file
def get_file_size(path):
    return os.path.getsize(path) / 1024000 # transform from bynary bytes to decimal megabytes

