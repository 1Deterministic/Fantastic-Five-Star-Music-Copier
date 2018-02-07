# general imports
import os.path

# this function returns the file extension of a file given in 'path'
def get_extension(path):
    return os.path.splitext(path)[1]

# this function returns true if the file given in 'path' is an audio file, and false if it isn't
def is_audio_file(path):
    # it only supports .mp3
    if get_extension(path) == ".mp3":
        return True
    else:
        return False

# this function returns a list of audio files present on a list of files of any type
def filter_audio_files(list):
    tmp = []

    for l in list:
        if is_audio_file(l):
            tmp.append(l)

    return tmp