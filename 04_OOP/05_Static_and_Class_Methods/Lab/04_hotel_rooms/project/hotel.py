from typing import List
from project.room import Room


class Hotel:
    def __init__(self, name: str):
        self.name = name
        self.guests = 0
        self.rooms: List[Room] = []

    @classmethod
    def from_stars(cls, stars_count: int):
        return cls(f"{stars_count} stars Hotel")

    def add_room(self, room: Room):
        self.rooms.append(room)

    def take_room(self, room_number: int, people: int):
        for r in self.rooms:
            if r.number == room_number:
                if not r.take_room(people):
                    self.guests += people

                break

    def free_room(self, room_number: int):
        for r in self.rooms:
            if r.number == room_number:
                self.guests -= r.guests
                r.free_room()

                break

    def status(self) -> str:
        free_rooms = []
        taken_rooms = []
        for r in self.rooms:
            if r.is_taken:
                taken_rooms.append(r.number)
            else:
                free_rooms.append(r.number)
        return (f"Hotel {self.name} has {self.guests} total guests\n"
                f"Free rooms: {', '.join(str(x) for x in free_rooms)}\n"
                f"Taken rooms: {', '.join(str(x) for x in taken_rooms)}")

