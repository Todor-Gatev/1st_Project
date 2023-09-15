from math import ceil
from typing import List


class PhotoAlbum:
    PHOTOS_ON_PAGE = 4

    def __init__(self, pages: int):
        self.pages = pages
        # self.photos: List = [[]] * pages
        self.photos: List = [[] for _ in range(self.pages)]

    @classmethod
    def from_photos_count(cls, photos_count: int):
        # pages = ceil(photos_count / 4)
        return cls(ceil(photos_count / cls.PHOTOS_ON_PAGE))

    def add_photo(self, label: str):
        for page in range(self.pages):
            if len(self.photos[page]) < PhotoAlbum.PHOTOS_ON_PAGE:
                self.photos[page].append(label)

                return f"{label} photo added successfully on page {page + 1} slot {len(self.photos[page])}"

        return "No more free slots"

    def display(self):
        result = f"{'-' * 11}\n"

        for page in self.photos:
            res = "[] " * len(page)
            result += res[:-1] + f"\n{'-' * 11}\n"

        return result


# album = PhotoAlbum(2)
#
# print(album.add_photo("baby"))
# print(album.add_photo("first grade"))
# print(album.add_photo("eight grade"))
# print(album.add_photo("party with friends"))
# print(album.photos)
# print(album.add_photo("prom"))
# print(album.add_photo("wedding"))
#
# print(album.display())
