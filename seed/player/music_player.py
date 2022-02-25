import subprocess

class MusicPlayer:

    def __init__(self, args):
        self.args = args

    def play(self, track):# will get passed a track file and will play it
        self.track = track # which will be an mp3 file name
        return self.args.call(["afplay", f"{self.track}"])

# The interface is doing the heavy lifting and interaction to check if track exists
