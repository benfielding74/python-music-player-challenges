import unittest

from player.music_library import MusicLibrary


class TestMusicLibrary(unittest.TestCase):
    def test_constructs(self):
        MusicLibrary()

    def test_adds_item_to_library(self):
        music_library = MusicLibrary()
        music_library.add("Rolling Blackouts by The Go! Team")
        self.assertEqual(music_library.trackList, ["Rolling Blackouts by The Go! Team"])

    def test_lists_songs_in_the_library(self):
        music_library = MusicLibrary()
        music_library.add("Rolling Blackouts by The Go! Team")
        music_library.add("Oh Yeah by Locust")
        self.assertEqual(music_library.all(), ["Rolling Blackouts by The Go! Team", "Oh Yeah by Locust"])

    def test_removes_songs_from_library(self):
        music_library = MusicLibrary()
        music_library.add("Rolling Blackouts by The Go! Team")
        music_library.add("Oh Yeah by Locust")
        music_library.remove(1)
        self.assertEqual(music_library.trackList, ["Rolling Blackouts by The Go! Team"])

    def test_returns_false_if_removing_song_not_in_list(self):
        music_library = MusicLibrary()
        self.assertFalse(music_library.remove(20))
