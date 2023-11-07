from typing import List

from project.band_members.musician import Musician


class Guitarist(Musician):
    MUSICIAN_TYPE = "Guitarist"

    @property
    def possible_skills(self) -> List[str]:
        return ["play metal", "play rock", "play jazz"]
