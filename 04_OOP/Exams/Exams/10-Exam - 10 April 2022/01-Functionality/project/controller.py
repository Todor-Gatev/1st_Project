class Controller:
    VALID_SUSTENANCE_TYPES = ["Food", "Drink"]

    def __init__(self):
        self.players = []
        self.supplies = []

    def add_player(self, *players):
        new_players = []

        for p in players:
            if p not in self.players:
                self.players.append(p)
                new_players.append(p.name)

        return f"Successfully added: {', '.join(new_players)}"

    def add_supply(self, *supplies):
        self.supplies.extend(supplies)

    def sustain(self, player_name: str, sustenance_type: str):
        player = next(filter(lambda x: x.name == player_name, self.players), None)

        if not player or sustenance_type not in Controller.VALID_SUSTENANCE_TYPES:
            return

        if not player.need_sustenance:
            return f"{player_name} have enough stamina."

        for i in range(len(self.supplies) - 1, -1, -1):
            if self.supplies[i].__class__.__name__ == sustenance_type:
                sustenance = self.supplies.pop(i)
                break
        else:
            raise Exception(f"There are no {sustenance_type.lower()} supplies left!")

        player.stamina = min(100, player.stamina + sustenance.energy)

        return f"{player_name} sustained successfully with {sustenance.name}."

    def duel(self, first_player_name: str, second_player_name: str):
        players = sorted(
            [next(filter(lambda x: x.name == first_player_name, self.players)),
             next(filter(lambda x: x.name == second_player_name, self.players))],
            key=lambda x: x.stamina)

        is_zero_stamina = [p.name for p in players if p.stamina == 0]

        if is_zero_stamina:
            return "\n".join(f"Player {name} does not have enough stamina." for name in is_zero_stamina)

        players[1].stamina -= players[0].stamina / 2
        players[0].stamina = max(0, players[0].stamina - (players[1].stamina / 2))

        if players[0].stamina < players[1].stamina:
            return f"Winner: {players[1].name}"
        else:
            return f"Winner: {players[0].name}"

    def next_day(self):
        for p in self.players:
            p.stamina = max(0, p.stamina - p.age * 2)
            self.sustain(p.name, "Food")
            self.sustain(p.name, "Drink")

    def __str__(self):
        res = [*[str(p) for p in self.players], *[s.details() for s in self.supplies]]
        return "\n".join(res)
