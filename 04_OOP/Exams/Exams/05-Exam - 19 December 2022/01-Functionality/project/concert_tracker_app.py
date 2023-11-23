from project.band import Band
from project.band_members.drummer import Drummer
from project.band_members.guitarist import Guitarist
from project.band_members.singer import Singer
from project.concert import Concert


class ConcertTrackerApp:
    MUSICIAN_TYPES = {"Guitarist": Guitarist, "Drummer": Drummer, "Singer": Singer}
    CONCERT_GENRE = {
        "Rock": {"Drummer": ["play the drums with drumsticks"],
                 "Singer": ["sing high pitch notes"],
                 "Guitarist": ["play rock"]},
        "Metal": {"Drummer": ["play the drums with drumsticks"],
                  "Singer": ["sing low pitch notes"],
                  "Guitarist": ["play metal"]},
        "Jazz": {"Drummer": ["play the drums with drum brushes"],
                 "Singer": ["sing high pitch notes", "sing low pitch notes"],
                 "Guitarist": ["play jazz"]}
    }

    def __init__(self):
        self.bands = []
        self.musicians = []
        self.concerts = []

    def create_musician(self, musician_type: str, name: str, age: int):
        if musician_type not in self.MUSICIAN_TYPES:
            raise ValueError("Invalid musician type!")

        if self.find_object(self.musicians, "name", name):
            raise Exception(f"{name} is already a musician!")

        self.musicians.append(self.MUSICIAN_TYPES[musician_type](name, age))

        return f"{name} is now a {musician_type}."

    def create_band(self, name: str):
        if self.find_object(self.bands, "name", name):
            raise Exception(f"{name} band is already created!")

        self.bands.append(Band(name))
        return f"{name} was created."

    def create_concert(self, genre: str, audience: int, ticket_price: float, expenses: float, place: str):
        concert = self.find_object(self.concerts, "place", place)

        if concert:
            raise Exception(f"{place} is already registered for {concert.genre} concert!")

        self.concerts.append(Concert(genre, audience, ticket_price, expenses, place))

        return f"{genre} concert in {place} was added."

    def add_musician_to_band(self, musician_name: str, band_name: str):
        musician = self.find_object(self.musicians, "name", musician_name)
        band = self.find_object(self.bands, "name", band_name)

        if not musician:
            raise Exception(f"{musician_name} isn't a musician!")

        if not band:
            raise Exception(f"{band_name} isn't a band!")

        if musician not in band.members:
            band.members.append(musician)

        return f"{musician_name} was added to {band_name}."

    def remove_musician_from_band(self, musician_name: str, band_name: str):
        band = self.find_object(self.bands, "name", band_name)
        # musician = self.find_object(band.members, "name", musician_name)

        if not band:
            raise Exception(f"{band_name} isn't a band!")

        musician = self.find_object(band.members, "name", musician_name)

        if not musician:
            raise Exception(f"{musician_name} isn't a member of {band_name}!")

        band.members.remove(musician)

        return f"{musician_name} was removed from {band_name}."

    def start_concert(self, concert_place: str, band_name: str):
        band = self.find_object(self.bands, "name", band_name)
        concert = self.find_object(self.concerts, "place", concert_place)

        if not self.is_in_band_all_type_musicians(band):
            raise Exception(f"{band_name} can't start the concert because it doesn't have enough members!")

        band_needed_skills_for_concert = self.CONCERT_GENRE[concert.genre]

        for member in band.members:
            member_needed_skills = band_needed_skills_for_concert[member.__class__.__name__]

            for member_needed_skill in member_needed_skills:
                if member_needed_skill not in member.skills:
                    raise Exception(f"The {band_name} band is not ready to play at the concert!")

        profit = (concert.audience * concert.ticket_price) - concert.expenses

        return f"{band_name} gained {profit:.2f}$ from the {concert.genre} concert in {concert_place}."

    # region supporting staff
    def is_in_band_all_type_musicians(self, band) -> bool:

        musician_types = set()

        for member in band.members:
            musician_types.add(member.__class__.__name__)

            if len(musician_types) == len(self.MUSICIAN_TYPES):
                return True

        return False

    @staticmethod
    def find_object(collection: list, attribute: str, value: str):
        for obj in collection:
            if str(getattr(obj, attribute)) == value:
                return obj
    # endregion
