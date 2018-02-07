# general imports
import sys
import shutil
import os.path
from os import walk
import logging

# project imports
import fileextension
from audiotag import Tag

# this function returns a list of music files rated as 5 stars inside 'path' folder and its subfolders
# it only supports .mp3 files. I've tested with ratings from MediaMonkey and Clementine and it appears to be working
def search(path):
    files = []

    for (dirpath, dirnames, filenames) in walk(path):
        for f in filenames:
            if fileextension.is_audio_file(f):
                if Tag(dirpath + "/" + f).rating == 5:
                    files.append(dirpath + "/" + f)

    return files

# this function returns a list of filenames without the path before its current directory
def extract_filenames(list):
    filenames = []

    for l in list:
        filenames.append(os.path.basename(l))

    return filenames

# this function returns a list of files existing on the 'path' folder
def existing_files_list(path):
    for (dirpath, dirnames, filenames) in walk(path):
        return filenames


#_______________________________________ Program starts here __________________________________________________#

if __name__ == "__main__":
    # ignores warnings from eyed3 (it throws A LOT of warnings :P)
    logging.getLogger("eyed3").setLevel(logging.CRITICAL)

    # getting and validating the folders
    try:
        if os.path.isdir(sys.argv[sys.argv.index("-source") + 1]) and os.path.isdir(
                sys.argv[sys.argv.index("-destination") + 1]):
            source_path = sys.argv[sys.argv.index("-source") + 1]
            destination_path = sys.argv[sys.argv.index("-destination") + 1]
        else:
            print("Some of the paths received is not a folder.")
            sys.exit()

    except:
        print("""Invalid arguments, must be:
ffsmc.exe -source "source_folder" -destination "destination_folder" [-override_on_destination] [-delete_left_files]
* Options between brackets are optional
* The argument after -source must be the source folder
* The argument after -destination must be the destination folder
* -override_on_destination copy/paste all files, overwriting those already on destination. If it's not received, it will copy/paste only the files needed
* -delete_left_files deletes all the files on destination that wasn't found on the source during the scan, or don't match the requisites to be selected (have a rating of 5 stars). If it's not received, they will be ignored
* You must use .exe extension even running on Linux. It is a peculiarity of standalone export using nuitka I kept
* Notice that, for now, the only equality check made in -override_on_destination and -delete_left_files is based on the file name
            """)
        sys.exit()

    # checking for the command to delete the left files
    try:
        if sys.argv.index("-delete_left_files"):
            delete_left_files = True

    except:
        delete_left_files = False

    # checking for the command to override the files on destination
    try:
        if sys.argv.index("-override_on_destination"):
            override_on_destination = True

    except:
        override_on_destination = False

    # removing the last slash or backslash from the paths, if they exist
    if source_path.endswith('/') or source_path.endswith('\\'):
        source_path = source_path[:-1]

    if destination_path.endswith('/') or destination_path.endswith('\\'):
        destination_path = destination_path[:-1]

    # finds all 5-star rating musics in the given source folder
    print("Scanning source folder...")
    file_list = search(source_path)

    # copy-paste all files selected, if they're not yet in the output folder or if override_on_destination was received
    if len(file_list) > 0: print("Copying new files:")
    for l in file_list:
        if (not os.path.isfile(destination_path + "/" + os.path.basename(l))) or override_on_destination:
            try:
                print("\t" + l)
                shutil.copy(l, destination_path)
            except:
                print("Error: file " + l + " was not copied.")
                print("Exiting for safety.")
                sys.exit()

    # if delete_left_files was received, the files that are not 5-stars anymore will be removed
    if delete_left_files:
        # getting a list of files to delete in destination folder
        source_list = set(extract_filenames(file_list))
        destination_list = set(
            extract_filenames(fileextension.filter_audio_files(existing_files_list(destination_path))))
        must_delete = destination_list - source_list

        # removing the left files
        if len(must_delete) > 0: print("Deleting left files:")
        for m in must_delete:
            try:
                print("\t" + m)
                os.remove(destination_path + "/" + m)
            except:
                print("Error: file " + m + " was not deleted.")

    print("Done!")
    sys.exit()
