from typing import List
from project.song import Song


class Album:
    def __init__(self, name: str, *songs):
        self.name = name
        self.published = False
        self.songs: List[Song] = list(songs)

    def add_song(self, song: Song) -> str:
        if song.single:
            return "Cannot add {song_name}. It's a single"

        if self.published:
            return "Cannot add songs. Album is published."

        if song in self.songs:
            return "Song is already in the album."

        self.songs.append(song)

        return f"Song {song.name} has been added to the album {self.name}."

    def remove(self, song_name: str) -> str:
        if self.published:
            return "Cannot remove songs. Album is published."

        for song_i in self.songs:
            if song_i.name == song_name:
                self.songs.remove(song_i)

                return f"Removed song {song_name} from album {self.name}."
        else:
            return "Song is not in the album."

    def publish(self) -> str:
        if self.published:
            return f"Album {self.name} is already published."

        self.published = True

        return f"Album {self.name} has been published."

    def details(self) -> str:
        return f"Album {self.name}\n" + "\n".join(f"== {s.get_info()}" for s in self.songs)
