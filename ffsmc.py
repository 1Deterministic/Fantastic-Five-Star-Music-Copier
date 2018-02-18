# general imports
import sys
import shutil
import os.path
import logging
import locale
from os import walk
from random import shuffle

# project imports
import strings
import fileextension
import filedirsize
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



################################################################################################################
################################################################################################################
######################################### Program starts here ##################################################
################################################################################################################
################################################################################################################

if __name__ == "__main__":
    # ignores warnings from eyed3 (it throws A LOT of warnings :P)
    logging.getLogger("eyed3").setLevel(logging.CRITICAL)


    # getting system language
    language = "en" # en is the default language
    if locale.getdefaultlocale()[0][:2] in strings.msg: # if the current language is supported, then it is set
        language = locale.getdefaultlocale()[0][:2]


    # shows the help screen, if -h is received anywhere in the arguments
    try:
        if (sys.argv.index("-h")):
            print(strings.msg[language]["help"])
            sys.exit()

    except SystemExit: # sys.exit also throws an exception, this catches it to properly close the program
        os._exit(0)

    except ValueError: # -h not received
        pass


    # getting and validating the folders
    try:
        if os.path.isdir(sys.argv[sys.argv.index("-source") + 1]) and os.path.isdir(
                sys.argv[sys.argv.index("-destination") + 1]):
            source_path = sys.argv[sys.argv.index("-source") + 1]
            destination_path = sys.argv[sys.argv.index("-destination") + 1]

        else: # some path received is not a folder
            print(strings.msg[language]["invalid path"])
            sys.exit()

    except ValueError: # missing -source or -destination
        print(strings.msg[language]["missing required arguments"])
        sys.exit()

    except IndexError: # missing path after -source or -destination
        print(strings.msg[language]["missing folder path"])
        sys.exit()

    except SystemExit: # sys.exit()
        os._exit(0)


    # checking for the command to delete the left files
    try:
        if sys.argv.index("-delete_left_files"):
            delete_left_files = True

    except ValueError: # -delete_left_files not received
        delete_left_files = False


    # checking for the command to override the files on destination
    try:
        if sys.argv.index("-override_on_destination"):
            override_on_destination = True

    except ValueError: # -override_on_destination not received
        override_on_destination = False


    # checking for the command to limit destination folder size
    try:
        if sys.argv.index("-size_limit"):
            if sys.argv[sys.argv.index("-size_limit") + 1].isdigit(): # must be a positive integer
                size_limit = int(sys.argv[sys.argv.index("-size_limit") + 1])

            else: # negative, not integer or not numerical value
                print(strings.msg[language]["invalid size"])
                sys.exit()

    except ValueError: # -size_limit not received
        size_limit = 0

    except IndexError: # missing size after -size_limit
        print(strings.msg[language]["missing size limit"])
        sys.exit()

    except SystemExit: # sys.exit()
        os._exit(0)


    # checking for the command to shuffle copied files order (will take effect if size_limit is used)
    try:
        if sys.argv.index("-shuffle_file_list"):
            shuffle_file_list = True

    except ValueError: # -shuffle_file_list not received
        shuffle_file_list = False


    # checking for the command to log copied and deleted files on the screen
    try:
        if sys.argv.index("-log"):
            log = True

    except ValueError: # -log not received
        log = False


    # removing the last slash or backslash from the paths, if they exist
    if source_path.endswith('/') or source_path.endswith('\\'):
        source_path = source_path[:-1]

    if destination_path.endswith('/') or destination_path.endswith('\\'):
        destination_path = destination_path[:-1]


    # finds all 5-star rating musics in the given source folder
    print(strings.msg[language]["scanning source"])
    file_list = search(source_path)

    # init a zero total size to increment when files are copied or skipped because they already exist (when -override_on_destination was not received)
    total_size = 0.0

    # shuffle file_list to randomize what is copied when size_limit is used
    if shuffle_file_list: shuffle(file_list)

    # copy-paste all files selected, if they're not yet in the output folder or if override_on_destination was received
    if len(file_list) > 0: print(strings.msg[language]["copying new files"])
    for l in file_list:
        if (not os.path.isfile(destination_path + "/" + os.path.basename(l))) or override_on_destination: # file doesnt exist or will be overwrited
            try:
                if log: print("\t" + l)
                shutil.copy(l, destination_path)

            except:
                print(strings.msg[language]["error"] + l + strings.msg[language]["not copied"])
                print(strings.msg[language]["safe exit"])
                sys.exit()

        if size_limit > 0: # size limited received
            try:
                total_size += filedirsize.get_file_size(destination_path + "/" + os.path.basename(l)) # update total size
                if total_size > size_limit: # size limit exceeded
                    print(strings.msg[language]["size limit reached"])
                    file_list = file_list[:file_list.index(l)] # cut file_list to properly delete left files
                    break

            except:
                print(strings.msg[language]["error"] + strings.msg[language]["copied file not found"])
                print(strings.msg[language]["safe exit"])
                sys.exit()


    # if delete_left_files was received, the files that are not 5-stars anymore will be removed
    if delete_left_files:
        # getting a list of files to delete in destination folder
        source_list = set(extract_filenames(file_list))
        destination_list = set(
            extract_filenames(fileextension.filter_audio_files(existing_files_list(destination_path))))
        must_delete = destination_list - source_list

        # removing the left files
        if len(must_delete) > 0: print(strings.msg[language]["deleting left files"])
        for m in must_delete:
            try:
                if log: print("\t" + m)
                os.remove(destination_path + "/" + m)

            except:
                print(strings.msg[language]["error"] + m + strings.msg[language]["not deleted"])


    print(strings.msg[language]["done"])
    sys.exit()