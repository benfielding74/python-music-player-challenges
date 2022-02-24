import unittest
from unittest.mock import Mock
from player.music_player import MusicPlayer

class TestMusicPlayer(unittest.TestCase):
    def test_constructs(self):
        MusicPlayer()

    def test_plays_a_track(self):
        
