import unittest
from player.music_library import MusicLibrary, Track



class TestMusicLibrary(unittest.TestCase):
    def test_constructs(self):
        MusicLibrary()

    def test_adds_item_to_library(self):
        music_library = MusicLibrary()
        music_library.add(Track("Rolling Blackouts", "The Go! Team", "rolling_blackouts.mp3"))
        self.assertEqual(music_library.trackList, [Track(title='Rolling Blackouts', artist='The Go! Team', file='rolling_blackouts.mp3')])

    def test_lists_songs_in_the_library(self):
        music_library = MusicLibrary()
        music_library.add(Track("Rolling Blackouts", "The Go! Team", "rolling_blackouts.mp3"))
        self.assertEqual(music_library.all(), [Track(title='Rolling Blackouts', artist='The Go! Team', file='rolling_blackouts.mp3')])

    def test_removes_songs_from_library(self):
        music_library = MusicLibrary()
        music_library.add(Track("Rolling Blackouts", "The Go! Team", "rolling_blackouts.mp3"))
        music_library.add(Track("Oh Yeah", "Locust", "oh_yeah.mp3"))
        music_library.remove(1)
        self.assertEqual(music_library.trackList, [Track(title='Rolling Blackouts', artist='The Go! Team', file='rolling_blackouts.mp3')])

    def test_returns_false_if_removing_song_not_in_list(self):
        music_library = MusicLibrary()
        self.assertFalse(music_library.remove(20))

class TestTrack(unittest.TestCase):
    def test_constructs(self):
        Track("The Boys of Summer", "DJ Sammy", "summer.mp3")

    def test_has_attributes_of_given_track(self):
        track = Track("Rolling Blackouts", "Go! Team", "rolling_blackouts.mp3")
        self.assertEqual(track.title, "Rolling Blackouts")
