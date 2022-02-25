import subprocess

class MusicPlayer:

    def __init__(self, args):
        self.args = args

    def play(self, track):
        self.track = track
        return self.args.call(["afplay", f"{self.track}"])
