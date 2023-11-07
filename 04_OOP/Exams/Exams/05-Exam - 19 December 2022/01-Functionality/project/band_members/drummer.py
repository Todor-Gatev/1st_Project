from typing import List

from project.band_members.musician import Musician


class Drummer(Musician):
    MUSICIAN_TYPE = "Drummer"

    @property
    def possible_skills(self) -> List[str]:
        return ["play the drums with drumsticks", "play the drums with drum brushes", "read sheet music"]
