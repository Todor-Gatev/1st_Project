class Controller:
    SUSTENANCE_TYPES = ["Food", "Drink"]

    def __init__(self):
        self.players = []
        self.supplies = []

    def __get_player_via_name(self, name):
        return next(filter(lambda x: x.name == name, self.players), None)

    def add_player(self, *args):
        added_names = []

        for p in args:
            if p not in self.players:
                added_names.append(p.name)
                self.players.append(p)

        return f"Successfully added: {', '.join(added_names)}"

    def add_supply(self, *args):
        [self.supplies.append(s) for s in args]

    def sustain(self, player_name: str, sustenance_type: str):
        player = self.__get_player_via_name(player_name)

        if not player:
            return

        if not player.need_sustenance:
            return f"{player_name} have enough stamina."

        if sustenance_type not in self.SUSTENANCE_TYPES:
            return

        supply = next(filter(lambda x: x.__class__.__name__ == sustenance_type, reversed(self.supplies)), None)

        if not supply:
            raise Exception(f"There are no {sustenance_type.lower()} supplies left!")

        player.stamina = min(100, player.stamina + supply.energy)

        for idx in range(len(self.supplies) - 1, -1, -1):
            if self.supplies[idx] == supply:
                self.supplies.pop(idx)
                break

        return f"{player_name} sustained successfully with {supply.name}."

    def duel(self, first_player_name: str, second_player_name: str):
        player1 = self.__get_player_via_name(first_player_name)
        player2 = self.__get_player_via_name(second_player_name)

        players_with_zero_stamina = [p.name for p in [player1, player2] if p.stamina == 0]

        if players_with_zero_stamina:
            return "\n".join(f"Player {name} does not have enough stamina." for name in players_with_zero_stamina)

        duelers = sorted([player1, player2], key=lambda p: p.stamina)

        duelers[1].stamina -= duelers[0].stamina / 2

        duelers[0].stamina = max(0, duelers[0].stamina - duelers[1].stamina / 2)

        duelers = sorted(duelers, key=lambda p: p.stamina)

        return f"Winner: {duelers[1].name}"

    def next_day(self):
        for p in self.players:
            p.stamina = max(0, p.stamina - p.age * 2)
            self.sustain(p.name, "Food")
            self.sustain(p.name, "Drink")

    def __str__(self):
        players_info = [str(p) for p in self.players]
        supply_info = [s.details() for s in self.supplies]

        return "\n".join([*players_info, *supply_info])
