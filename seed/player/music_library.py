class MusicLibrary:

    def __init__(self):
        self.trackList = []

    def add(self, track):
        self.track = track
        self.trackList.append(self.track)

    def remove(self, track):
        self.track = track
        if self.track < len(self.trackList):
            del self.trackList[self.track]
            return True
        else:
            return False

    def all(self):
        return self.trackList

from dataclasses import dataclass

@dataclass
class Track:
    """Class for keeping track of song data."""
    title: str
    artist: str
    file: str
