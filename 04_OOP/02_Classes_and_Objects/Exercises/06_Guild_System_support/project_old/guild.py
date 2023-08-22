from typing import List

from project.player import Player


# from project_old.player import Player
#
#
class Guild:
    all_players: List[Player] = []

    def __init__(self, name: str):
        self.name = name
        self.players: List[Player] = []

    def assign_player(self, player: Player):
        if player in self.players:
            return f"Player {player.name} is already in the guild."

        if player in Guild.all_players:
            return f"Player {player.name} is in another guild."

        self.players.append(player)
        Guild.all_players.append(player)
        player.guild = self.name

        return f"Welcome player {player.name} to the guild {self.name}"

    def kick_player(self, player_name: str):
        for guild_player in self.players:
            if guild_player.name == player_name:
                self.players.remove(guild_player)
                Guild.all_players.remove(guild_player)
