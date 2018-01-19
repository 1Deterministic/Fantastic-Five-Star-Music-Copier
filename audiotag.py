# awesome lib for dealing with tags. I just had some problems finding where the h*ck the ratings where stored xD
import eyed3
import math


# a class for manipulating the tags more object-oriented
class Tag:

    # the class constructor receives the path for the music file
    def __init__(self, path):
        # tries to read the file
        try:
            # loads the file
            self.file = eyed3.load(path)

            # loads the properties
            self.artist = self.file.tag.artist
            self.album = self.file.tag.album
            self.title = self.file.tag.title
            self.rating = math.ceil(self.file.tag.frame_set[b'POPM'][0].rating / 51)

        except:
            # sets null values to its properties
            self.artist = "<none>"
            self.album = "<none>"
            self.title = "<none>"
            self.rating = 0

