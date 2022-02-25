import unittest
import subprocess
from unittest.mock import Mock
from player.music_player import MusicPlayer

class TestMusicPlayer(unittest.TestCase):
    def test_constructs(self):
        MusicPlayer(subprocess)

    def test_plays_a_track(self):
        #mock_track = Mock('data/tunes/myfav.wav') # should I also mock the player?
        #music_player = MusicPlayer(subprocess)
        fake_player = Mock()
        #self.assertEqual(music_player.play(mock_track), 0)
        fake_player.play = Mock(return_value=0)
        self.assertEqual(fake_player.play('data/tunes/myfav.wav'), 0)
