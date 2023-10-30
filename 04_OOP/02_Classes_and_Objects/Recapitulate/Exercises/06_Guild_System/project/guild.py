from typing import List
from project.player import Player


class Guild:
    def __init__(self, name: str):
        self.name = name
        self.players: List[Player] = []

    def assign_player(self, player_n: Player) -> str:
        if player_n.guild != Player.PLAYER_DEFAULT_GUILD:
            return f"Player {player_n.name} is in another guild."

        if player_n in self.players:
            return f"Player {player_n.name} is already in the guild."

        self.players.append(player_n)
        player_n.guild = self.name

        return f"Welcome player {player_n.name} to the guild {self.name}"

    def kick_player(self, player_name: str) -> str:
        for p in self.players:
            if p.name == player_name:
                p.guild = Player.PLAYER_DEFAULT_GUILD

                return f"Player {player_name} has been removed from the guild."
        else:
            return f"Player {player_name} is not in the guild."

    def guild_info(self) -> str:
        return f"Guild: {self.name}\n" + "\n".join(p.player_info() for p in self.players)


player = Player("George", 50, 100)
print(player.add_skill("Shield Break", 20))
print(player.player_info())
guild = Guild("UGT")
print(guild.assign_player(player))
print(guild.guild_info())
