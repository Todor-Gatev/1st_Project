from project.player import Player
from typing import List


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
#
# kick_player(player_name: str)
# Removes the player from the guild and returns
# "Player {player_name} has been removed from the guild.".
# Remember to change the player's guild in the player class to "Unaffiliated".
# If there is no such player in the guild, returns
# "Player {player_name} is not in the guild."
#
# guild_info()
# Returns the guild's information, including the players in the guild, in the format:
# "Guild: {guild_name}
# {first_player's info}
# …
# {Nplayer's info}"

# player = Player("George", 50, 100)
# print(player.add_skill("Shield Break", 20))
# print(player.player_info())
# guild = Guild("UGT")
# print(guild.assign_player(player))
# print(guild.guild_info())
