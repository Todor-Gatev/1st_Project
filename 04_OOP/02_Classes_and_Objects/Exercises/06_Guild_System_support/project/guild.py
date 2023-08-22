from typing import List
from project.player import Player


class Guild:
    # all_players: List[Player] = []

    def __init__(self, name: str):
        self.name = name
        self.players: List[Player] = []

    def assign_player(self, player: Player) -> str:
        # if player in self.players:
        if player.guild == self.name:
            return f"Player {player.name} is already in the guild."

        if player.guild != Player.PLAYER_DEFAULT_GUILD:
            return f"Player {player.name} is in another guild."

        self.players.append(player)
        # Guild.all_players.append(player)
        player.guild = self.name

        return f"Welcome player {player.name} to the guild {self.name}"

    def kick_player(self, player_name: str):
        for player in self.players:
            if player.name == player_name:
                self.players.remove(player)
                player.guild = Player.PLAYER_DEFAULT_GUILD
                # Guild.all_players.remove(guild_player)

                return f"Player {player_name} has been removed from the guild."

        return f"Player {player_name} is not in the guild."

    def guild_info(self) -> str:
        players_info = '\n'.join([p.player_info() for p in self.players])
        return f"Guild: {self.name}\n" \
               f"{players_info}"


player = Player("George", 50, 100)
print(player.add_skill("Shield Break", 20))
print(player.player_info())
guild = Guild("UGT")
print(guild.assign_player(player))
print(guild.guild_info())
