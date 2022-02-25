import unittest
import subprocess
from unittest.mock import Mock
from player.music_player import MusicPlayer

class TestMusicPlayer(unittest.TestCase):
    def test_constructs(self):
        MusicPlayer(subprocess)

    def test_plays_a_track(self):
        mock_track = Mock('data/tunes/myfav.wav') # should I also mock the player?
        music_player = MusicPlayer(subprocess)
        self.assertEqual(music_player.play(mock_track), 0)
