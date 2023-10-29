from typing import List

from project.room import Room


class Hotel:
    def __init__(self, name: str):
        self.name = name
        self.rooms: List[Room] = []
        self.guests = 0

    @classmethod
    def from_stars(cls, stars_count: int):
        return cls(f"{stars_count} stars Hotel")

    @staticmethod
    def find_object(collection: list, attribute: str, value: str):
        for obj in collection:
            if str(getattr(obj, attribute)) == value:
                return obj

    def add_room(self, room: Room):
        self.rooms.append(room)

    def take_room(self, room_number: int, people: int) -> (str, None):
        r = self.find_object(self.rooms, "number", str(room_number))

        if not r.take_room(people):
            self.guests += people

    def free_room(self, room_number: int) -> (str, None):
        r = self.find_object(self.rooms, "number", str(room_number))
        self.guests -= r.guests
        r.free_room()

    def status(self) -> str:
        free_rooms_num = []
        taken_rooms_num = []

        for r in self.rooms:
            if r.is_taken:
                taken_rooms_num.append(str(r.number))
            else:
                free_rooms_num.append(str(r.number))

        return (f"Hotel {self.name} has {self.guests} total guests\n"
                f"Free rooms: {', '.join(free_rooms_num)}\n"
                f"Taken rooms: {', '.join(taken_rooms_num)}")
