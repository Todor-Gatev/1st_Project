from typing import List

from project.album import Album
from project.song import Song


class Band:
    def __init__(self, name: str):
        self.name = name
        self.albums: List[Album] = []

    def add_album(self, album_i: Album) -> str:
        if album_i in self.albums:
            return f"Band {self.name} already has {album_i.name} in their library."

        self.albums.append(album_i)

        return f"Band {self.name} has added their newest album {album_i.name}."

    def remove_album(self, album_name: str) -> str:
        for album_i in self.albums:
            if album_i.name == album_name:
                if album_i.published:
                    return "Album has been published. It cannot be removed."

                self.albums.remove(album_i)

                return f"Album {self.name} has been removed."

        return f"Album {self.name} is not found."

    def details(self) -> str:
        return f"Band {self.name}\n" + "\n".join(f"{a.details()}" for a in self.albums)


song = Song("Running in the 90s", 3.45, False)
print(song.get_info())
album = Album("Initial D", song)
second_song = Song("Around the World", 2.34, False)
print(album.add_song(second_song))
print(album.details())
print(album.publish())
band = Band("Manuel")
print(band.add_album(album))
print(band.remove_album("Initial D"))
print(band.details())
