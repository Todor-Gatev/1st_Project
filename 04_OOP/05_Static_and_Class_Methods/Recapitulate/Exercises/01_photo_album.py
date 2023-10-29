from math import ceil
from typing import List


class PhotoAlbum:
    PHOTOS_PER_PAGE = 4

    def __init__(self, pages: int):
        self.pages = pages
        self.photos: List[List[str]] = [[] for _ in range(self.pages)]

    @classmethod
    def from_photos_count(cls, photos_count: int):
        return cls(ceil(photos_count / cls.PHOTOS_PER_PAGE))

    def add_photo(self, label: str) -> str:
        if len(self.photos[-1]) == PhotoAlbum.PHOTOS_PER_PAGE:
            return "No more free slots"

        for idx in range(self.pages):
            if len(self.photos[idx]) < PhotoAlbum.PHOTOS_PER_PAGE:
                self.photos[idx].append(label)

                return f"{label} photo added successfully on page {idx + 1} slot {len(self.photos[idx])}"

    def display(self) -> str:
        s = '-' * 11
        result = [f"{s}\n" + f"{'[] ' * len(p)}"[:-1] for p in self.photos]

        return "\n".join(result) + f"\n{s}"


album = PhotoAlbum(2)

print(album.add_photo("baby"))
print(album.add_photo("first grade"))
print(album.add_photo("eight grade"))
print(album.add_photo("party with friends"))
print(album.photos)
print(album.add_photo("prom"))
print(album.add_photo("wedding"))

print(album.display())
